class Rational {
    private:
    int num; 
    int denom; 
    public: 
    
    Rational(int n, int d);
    Rational(const Rational& arg); // copy konstruktors - NAV OBLIGĀTS (dabū arī tāpat)
    ~Rational();

    //  r1.pieskaitit(r2);
    // es neko negribu dabūt atpakaļ -> atgriežamā vērtība ir void. 
    // viens no saskaitāmajiem bija "current object"; "this" - tam pieskaita klāt
    void pieskaitit(Rational arg);

    // divus argumentus sareizināt - un atgriežat trešo (bet nebojājat argumentus)
    // static == šai metodei "current object" nevajag vispār
    static Rational reizinat(Rational q1, Rational q2) {
        int newNum = q1.num * q2.num;
        int newDenom = q1.denom * q2.denom;
        return Rational(newNum, newDenom);
    }

    void drukat();
};
