#include <stdio.h>

#include "huriko.hpp"


int main()
{
    unsigned long prec;
	printf("input default prec in bits: "); scanf("%lu", &prec);
    mpreal::set_default_prec((mpfr_prec_t)prec);
    
    Param<mpreal> param;
    param.m1 = 5.2;
    param.m2 = 5.2;
    param.l1 = 1.4;
    param.l2 = 1.2;
    param.g = 9.8;
    param.start_theta1 = const_pi();
    param.start_theta2 = const_pi()/2;
    param.start_omega1 = 0.0;
    param.start_omega2 = 0.0;
    param.T = 60;
    param.n = 59999;
    param.h = param.T/param.n;

    dim1<mpreal> U(4 * (param.n + 1));

    solve_with_runge_kutta(U, param);

    FILE* f = fopen("output.txt", "w");
    for(int i = 0; i < param.n + 1; ++i)
    {
        fprintf(f, "%.9f %.9f\n", (double)U[4 * i + 0], (double)U[4 * i + 1]);
    }
    fclose(f);
}