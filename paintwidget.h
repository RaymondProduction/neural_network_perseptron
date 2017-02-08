#ifndef PAINTWIDGET_H
#define PAINTWIDGET_H

#include <QtGui>
#include <QtCore>
#include <QWidget>

class PaintWidget : public QWidget
{
    Q_OBJECT

public:
    PaintWidget(QWidget *parent = 0);
    ~PaintWidget();
protected:
    virtual void mousePressEvent(QMouseEvent *event);
    virtual void mouseMoveEvent(QMouseEvent *event);
    virtual void paintEvent(QPaintEvent *event);

    void savetomatrix(QMouseEvent *event);
    void delete_elment(QMouseEvent *event);



public slots:
    void align_matrix();
    void clear_matrix();
    void perseptron(); //нейрон (в будущем отдельный класс)
    void save_weights(); //запись весов
    void load_weights(); //загрузка весов
    void random_weights(); //случайные веса
private:
    int n;
    float speed;
    int matrix[20][20];
    float weights[20][20];
    bool mDrawMode;
};

#endif // PAINTWIDGET_H
