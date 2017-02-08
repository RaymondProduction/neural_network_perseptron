#include "paintwidget.h"


#include <QtCore/QLine>
#include <QtGui/QPainter>
#include <QtGui/QMouseEvent>
#include <QMessageBox>
#include <QFile>
#include <QTextStream>

PaintWidget::PaintWidget(QWidget *parent)
    : QWidget(parent)
{
    n=20;
    mDrawMode = false;
    speed=0.7;
    for (int j=0;j<n;j++){
     for (int i=0;i<n;i++) {
         matrix[i][j]=0;
         weights[i][j]=(float)(-3+qrand()%6)/10;
     }
    };

}

PaintWidget::~PaintWidget()
{

}

void PaintWidget::mousePressEvent(QMouseEvent *event)
{
    if (event->button() == Qt::LeftButton) {
        mDrawMode = true;
        savetomatrix(event);
        this->update();
        event->accept();
    }
    if (event->button() == Qt::RightButton) {
        delete_elment(event);
        this->update();
        event->accept();
    }
}

void PaintWidget::mouseMoveEvent(QMouseEvent *event)
{
    if (!mDrawMode) return;
    savetomatrix(event);
    this->update();
    event->accept();
}

void PaintWidget::paintEvent(QPaintEvent *event)
{
    QPainter painter(this);
    painter.setPen(Qt::green);
    painter.setBrush(QBrush(Qt::red));
    for (int j=0;j<n;j++) {
        for (int i=0; i<n; ++i) {
            if (matrix[i][j]==1) painter.drawRect(QRect(i*10,j*10,10,10));
        }
    }
    painter.setPen(QPen(Qt::black,2));
        for (int i=0;i<=20;i++){
            painter.drawLine(QPoint(i*10,0),QPoint(i*10,200));
            painter.drawLine(QPoint(0,i*10),QPoint(200,i*10));
        }

}

void PaintWidget::savetomatrix(QMouseEvent *event)
{
    int x=int(event->pos().x()/10);
    int y=int(event->pos().y()/10);
    if (x<n && y<n &&x >=0 && y>=0) matrix[x][y]=1;
}

void PaintWidget::delete_elment(QMouseEvent *event)
{
     int x=int(event->pos().x()/10);
     int y=int(event->pos().y()/10);
     if (x<n && y<n && x>=0 && y>=0) matrix[int(event->pos().x()/10)][int(event->pos().y()/10)]=0;
}

void PaintWidget::align_matrix()
{
    int i,j,xmin,xmax,ymin,ymax;
    int tmp[20][20];
    for (j=0;j<n;j++)
        for (i=0;i<n;i++) tmp[i][j]=0;

    xmin=n;xmax=-1;ymin=n;ymax=-1;

    for (j=0;j<n;j++){
        for (i=0;i<n;i++) {
            if (matrix[i][j]==1){
                if (i<xmin) xmin=i;
                if (i>xmax) xmax=i;
                if (j<ymin) ymin=j;
                if (j>ymax) ymax=j;
            }
        }
    }

    float xx,yy;
    for (j=0;j<n;j++){
        for (i=0;i<n;i++) {
            xx=(float)i/n*(xmax-xmin+1);
            yy=(float)j/n*(ymax-ymin+1);
            tmp[i][j]=matrix[xmin+(int)xx][ymin+(int)yy];
        }
    }
    for (j=0;j<n;j++)
        for (i=0;i<n;i++) matrix[i][j]=tmp[i][j];
    this->update();
}

void PaintWidget::clear_matrix()
{
    for (int j=0;j<n;j++){
     for (int i=0;i<n;i++) matrix[i][j]=0;
     };
    this->update();
}

void PaintWidget::perseptron()
{
    float sum; //вход персептрона
    short int rety;  //полученый выход персептрона
    short int test; //направление корректировки вестов (+1 или -1)
    QMessageBox* pmbx;

    sum=0;
    align_matrix(); //растягивание изображение на сетке ее границ

    for (int j=0;j<n;j++){
     for (int i=0;i<n;i++) sum+=matrix[i][j]*weights[i][j];
     };
    if (sum>0) {rety=1;} else {rety=0;};
    if (rety==1) {
      pmbx = new QMessageBox(QMessageBox::Question,"Question","X?",QMessageBox::Yes|QMessageBox::No);
    } else {
      pmbx = new QMessageBox(QMessageBox::Question,"Question","O?",QMessageBox::Yes|QMessageBox::No);
    }
     int answ = pmbx->exec();
     delete pmbx;
     if (answ==QMessageBox::No) {
         if (rety==0) {test=1;} else {test=-1;};
         for (int j=0;j<n;j++){
          for (int i=0;i<n;i++) weights[i][j]=weights[i][j]+(float)speed*test*matrix[i][j];
          };
     }
}
void PaintWidget::save_weights(){
    QFile file("weights.dat");
    if (file.open((QIODevice::WriteOnly))){
        QTextStream stream(&file);
        for (int j=0;j<n;j++){
         for (int i=0;i<n;i++) stream<<weights[i][j]<<"\t";
         stream<<"\n";
         };
    }
    file.close();
}
void PaintWidget::load_weights(){

    QFile file("weights.dat");
    QStringList strlist;

    if (file.open((QIODevice::ReadOnly))){
        QTextStream stream(&file);
        for (int j=0;j<n;j++){
            strlist=stream.readLine().split("\t");
         for (int i=0;i<n;i++) {
             weights[i][j]=strlist[i].toFloat();
         }
        };

    }
    file.close();
}
void PaintWidget::random_weights(){
    for (int j=0;j<n;j++){
     for (int i=0;i<n;i++) {
         weights[i][j]=(float)(-3+qrand()%6)/10;
     }
    };
}
