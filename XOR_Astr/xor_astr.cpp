#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <cstring>


class Astr {
  public:
    using key_t = uint32_t;
    static constexpr int mod = 1<<15;
    static_assert(mod == 32768);

    static key_t gen_key() {
        srand(time(NULL));
        key_t key = 0;
        auto sa = (uint16_t*)&key;
        sa[0] = rand() % mod;
        sa[1] = rand() % mod;
        return key;
    }

  private:
    key_t key = 0;

  public:
    void set_key(key_t k) { this->key = k; }

    std::string enc(std::string const& str, bool is_print=false) {
        int size = str.size();
        if ( ! size )
            return "";
        int mn = size / 4;
        if ( size % 4 )
            mn++;
        int arr_size = mn * 4;
        auto arr = (int*)new char[arr_size+1];
        memset(arr, 0, arr_size+1);
        strcpy((char*)arr, str.c_str());
        if ( is_print )
            std::cout<< "[";
        for (int i=0; i<mn; ++i) {
            arr[i] ^= this->key;
            if ( is_print ) {
                std::cout<< arr[i];
                if (i+1 < mn)
                    std::cout<< ", ";
            }
        }
        if ( is_print )
            std::cout<< "]" << std::endl;
        return std::string{(char*)arr};
    }
};



int main() {
    Astr astr;
    astr.set_key(1728069913);

    astr.enc("shutdown -h", true);

    int arr[] = {326445418, 158805629, 1734896697, 0};
    std::string str{(char*)arr};
    auto dstr = astr.enc(str);
    std::cout<< dstr << std::endl;

    std::cout << Astr::gen_key() << std::endl;
}


