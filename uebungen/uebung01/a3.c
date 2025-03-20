#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 30

typedef struct {
    int rows;
    int cols;
    int data[MAX][MAX];
} Matrix;


void initMatrix(Matrix* mat, int m, int n) {
    mat->rows = m;
    mat->cols = n;
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            mat->data[i][j] = 0;
        }
    }
}


void printMatrix(const Matrix* mat) {
    printf("Matrix (%dx%d):\n", mat->rows, mat->cols);
    for(int i = 0; i < mat->rows; i++) {
        for(int j = 0; j < mat->cols; j++) {
            printf("%d ", mat->data[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}


void inputMatrix(Matrix* mat) {
    printf("%d x %d:\n", mat->rows, mat->cols);
    for(int i = 0; i < mat->rows; i++) {
        for(int j = 0; j < mat->cols; j++) {
            scanf("%d", &(mat->data[i][j]));
        }
    }
}


void randomFillMatrix(Matrix* mat, int minVal, int maxVal) {
    for(int i = 0; i < mat->rows; i++) {
        for(int j = 0; j < mat->cols; j++) {
            mat->data[i][j] = minVal + rand() % (maxVal - minVal + 1);
        }
    }
}


Matrix add(const Matrix* A, const Matrix* B) {
    Matrix result;
    initMatrix(&result, A->rows, A->cols);
    for(int i = 0; i < A->rows; i++) {
        for(int j = 0; j < A->cols; j++) {
            result.data[i][j] = A->data[i][j] + B->data[i][j];
        }
    }
    return result;
}

Matrix mult(const Matrix* A, const Matrix* B) {
    Matrix result;
    initMatrix(&result, A->rows, B->cols);
    for(int i = 0; i < A->rows; i++) {
        for(int j = 0; j < B->cols; j++) {
            int sum = 0;
            for(int k = 0; k < A->cols; k++) {
                sum += A->data[i][k] * B->data[k][j];
            }
            result.data[i][j] = sum;
        }
    }
    return result;
}


int main(void) {
    srand((unsigned int)time(NULL));

    Matrix A, B, C;

    initMatrix(&A, 3, 3);
    initMatrix(&B, 3, 3);

    randomFillMatrix(&A, -5, 5);
    randomFillMatrix(&B, -5, 5);
//    inputMatrix(&A);
//    inputMatrix(&B);

    printf("Matrix A:\n");
    printMatrix(&A);

    printf("Matrix B:\n");
    printMatrix(&B);

    printf("A + B:\n");
    C = add(&A, &B);
    printMatrix(&C);

    printf("A * B:\n");
    C = mult(&A, &B);
    printMatrix(&C);

    return 0;
}
