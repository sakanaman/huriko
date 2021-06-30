#ifndef _HURIKO_HPP_
#define _HURIKO_HPP_


#include "mpreal.h"
#include <vector>

using namespace mpfr;

template<class Real>
class Param
{
public:
        Param(){}
        Real m1, m2, l1, l2, g, 
                start_theta1, start_theta2, s,
                start_omega1, start_omega2, T, h;
        int n;
};


template<class Real>
Real f1(const Real& c)
{
    return c;
}

template<class Real>
Real f2(const Real& d)
{
    return d;
}

template<class Real>
Real f3(const Real& a, const Real& b, 
        const Real& c, const Real& d, const Param<Real>& param)
{
        Real det_under = (param.m1 + param.m2)* param.l1 * param.l2 * param.l2 
                        - param.m2*param.l1 * param.l2 * param.l2 * cos(a - b) * cos(a - b);

        Real A = -param.m2 * param.l2 * d * d * sin(a - b) 
                - (param.m1 + param.m2) * param.g * sin(a);

        Real B = param.m2 * param.l2 * cos(a - b);
        Real C =  param.l1 * param.l2 * c * c * sin(a - b) 
                - param.g * param.l2 * sin(b);
        Real D = param.l2 * param.l2;

        Real det_above =  A*D - B*C;

        return det_above/det_under;
}


template<class Real>
Real f4(const Real& a, const Real& b, const Real& c, const Real& d, const Param<Real>& param)
{
        Real det_under = (param.m1 + param.m2) * param.l1 * param.l2 * param.l2 
                        - param.m2 * param.l1 * param.l2 * param.l2 * cos(a - b)*cos(a - b);

        Real A = (param.m1 + param.m2) * param.l1;
        Real B = -param.m2 * param.l2 * d * d * sin(a - b) 
                - (param.m1 + param.m2) * param.g * sin(a);
        Real C = param.l1 * param.l2 * cos(a - b);
        Real D =  param.l1 * param.l2 * c * c * sin(a - b) 
                - param.g * param.l2 * sin(b);
        Real det_above = A*D - B*C;

        return det_above/det_under;
}

template<class Real>
void f(Real &ret1, Real& ret2, Real& ret3, Real& ret4,
        const Real& a, const Real& b, const Real& c, const Real& d, 
        const Param<Real>& param)
{
        ret1 = f1(c);
        ret2 = f2(d);
        ret3 = f3(a, b, c, d, param);
        ret4 = f4(a, b, c, d, param);
}

template<class Real>
using dim1 = std::vector<Real>;

template<class Real>
void solve_with_runge_kutta(dim1<Real>& U, const Param<Real>& param)
{
        Real alpha = (Real)1.0 / (Real)8.0;
        Real delta = (Real)1.0 / (Real)8.0;
        Real beta = (Real)3.0 / (Real)8.0;
        Real ganma = (Real)3.0 / (Real)8.0;
        Real p = (Real)1.0 / (Real)3.0;
        Real q = (Real)1.0 / (Real)3.0;
        Real t = (Real)(-1.0) / (Real)3.0;
        Real r = (Real)2.0 / (Real)3.0;
        Real s = (Real)1.0;
        Real u = (Real)1.0;
        Real v = (Real)1.0;
        Real z = (Real)1.0;
        Real w = (Real)(-1.0);

        int n = (U.size() - 1)/4;
        U[0] = param.start_theta1;
        U[1] = param.start_theta2;
        U[2] = param.start_omega1;
        U[3] = param.start_omega2;

        dim1<Real> ui(4, (Real)0);
        dim1<Real> k1(4, (Real)0);
        dim1<Real> k2(4, (Real)0);
        dim1<Real> k3(4, (Real)0);
        dim1<Real> k4(4, (Real)0);
        dim1<Real> param2(4, (Real)0);
        dim1<Real> param3(4, (Real)0);
        dim1<Real> param4(4, (Real)0);

        for(int i = 0; i < n; ++i)
        {
                ui[0] = U[4 * i + 0];
                ui[1] = U[4 * i + 1];
                ui[2] = U[4 * i + 2];
                ui[3] = U[4 * i + 3];

                f(k1[0], k1[1], k1[2], k1[3],
                  ui[0], ui[1], ui[2], ui[3], param);
                
                param2[0] = ui[0] + q * param.h * k1[0];
                param2[1] = ui[1] + q * param.h * k1[1];
                param2[2] = ui[2] + q * param.h * k1[2];
                param2[3] = ui[3] + q * param.h * k1[3];
                f(k2[0], k2[1], k2[2], k2[3],
                param2[0],param2[1],param2[2],param2[3], param);


                param3[0] = ui[0] + s * param.h * k2[0] + t * param.h * k1[0];
                param3[1] = ui[1] + s * param.h * k2[1] + t * param.h * k1[1];
                param3[2] = ui[2] + s * param.h * k2[2] + t * param.h * k1[2];
                param3[3] = ui[3] + s * param.h * k2[3] + t * param.h * k1[3];
                f(k3[0], k3[1], k3[2], k3[3],
                param3[0],param3[1],param3[2],param3[3],param);

                param4[0] = ui[0] + v * param.h * k3[0]  + w * param.h * k2[0] + z * param.h * k1[0];
                param4[1] = ui[1] + v * param.h * k3[1]  + w * param.h * k2[1] + z * param.h * k1[1];
                param4[2] = ui[2] + v * param.h * k3[2]  + w * param.h * k2[2] + z * param.h * k1[2];
                param4[3] = ui[3] + v * param.h * k3[3]  + w * param.h * k2[3] + z * param.h * k1[3];
                f(k4[0], k4[1], k4[2], k4[3],
                param4[0],param4[1],param4[2],param4[3],param);

                U[4 * (i + 1) + 0] = ui[0] + param.h * (alpha * k1[0] + beta * k2[0] + ganma * k3[0] + delta * k4[0]);
                U[4 * (i + 1) + 1] = ui[1] + param.h * (alpha * k1[1] + beta * k2[1] + ganma * k3[1] + delta * k4[1]);
                U[4 * (i + 1) + 2] = ui[2] + param.h * (alpha * k1[2] + beta * k2[2] + ganma * k3[2] + delta * k4[2]);
                U[4 * (i + 1) + 3] = ui[3] + param.h * (alpha * k1[3] + beta * k2[3] + ganma * k3[3] + delta * k4[3]);
        }
}




#endif