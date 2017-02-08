#include <QApplication>
#include "paintwidget.h"
#include <QPushButton>
#include <QtGui>
#include <QLayout>
#include <QMessageBox>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);




    QWidget wgt;
    PaintWidget* w = new PaintWidget();
    QPushButton *Button1= new QPushButton("Clear");
    QPushButton *Button2= new QPushButton("Align");
    QPushButton *Button3= new QPushButton("Random weights");
    QPushButton *Button4= new QPushButton("Сheck");
    QPushButton *Button5= new QPushButton("Loading weights");
    QPushButton *Button6= new QPushButton("Save weights");

    QBoxLayout* pbxLayout = new QBoxLayout(QBoxLayout::LeftToRight);
    QBoxLayout* pvbxLayout = new QVBoxLayout;
    pvbxLayout->addWidget(Button1);
    pvbxLayout->addWidget(Button2);
    pvbxLayout->addWidget(Button3);
    pvbxLayout->addWidget(Button4);
    pvbxLayout->addWidget(Button5);
    pvbxLayout->addWidget(Button6);

    QObject::connect(Button1,SIGNAL(clicked()),w, SLOT(clear_matrix()));
    QObject::connect(Button2,SIGNAL(clicked()),w, SLOT(align_matrix()));
    QObject::connect(Button3,SIGNAL(clicked()),w, SLOT(random_weights()));
    QObject::connect(Button4,SIGNAL(clicked()),w, SLOT(perseptron()));
    QObject::connect(Button5,SIGNAL(clicked()),w, SLOT(load_weights()));
    QObject::connect(Button6,SIGNAL(clicked()),w, SLOT(save_weights()));


    pbxLayout->addWidget(w,2);
    pbxLayout->addLayout(pvbxLayout,1);
    wgt.setLayout(pbxLayout);
    wgt.resize(370,230);
    wgt.setWindowTitle("Raymond - Neural network");
    wgt.show();
    return app.exec();
}
