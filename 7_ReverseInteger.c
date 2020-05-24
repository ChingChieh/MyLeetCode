int reverse(int x){
    int result = x;
    unsigned long int Ux = 0;
    int i = 0;
    int negative = (x < 0);
    int buf[11] = {};
    
    if (x == INT_MIN) { // Take care of the corner case
        return 0;
    }
    x = negative ? x * (-1): x;
    
    for(; x > 0; x /= 10, ++i){
        buf[i + 1] = buf[i];
        buf[i] = x % 10;
    }
	
    for(int j = i; i > 0; --i){
        Ux += (unsigned long int)buf[j - i] * power10(i - 1); // Two integers multiplication can't exceed the INT_MAX
    }														  // That's why I need to cast one integer					
    if (Ux > (unsigned int)INT_MAX + negative){ // Again, remember to cast
        return 0;
    }
    result = (int)Ux;
    result = negative ? result * (-1): result; 
    return result;
}

int power10(int i){
    int mulTen = 1;    
    for(; i > 0; --i){
        mulTen *= 10;
    }
    return mulTen;
}


