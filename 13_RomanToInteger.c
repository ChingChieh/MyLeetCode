int romanToInt(char * s){
    int i = strlen(s) - 1;
    int count = 0;
    char prev = '\0';
    for(; i >= 0; --i){
        
        switch (s[i]) {
            case 'I':
                if (prev == 'V' | prev == 'X') count--;
                else count++;
                break;
            case 'V':
                count += 5;
                break;
            case 'X':
                if (prev == 'L' | prev == 'C') count -= 10;
                else count += 10;
                break;
            case 'L':
                count += 50;
                break;
            case 'C':
                if (prev == 'D' | prev == 'M') count -= 100;
                else count += 100;
                break;
            case 'D':
                count += 500;
                break;
            case 'M':
                count += 1000;
                break;
            default:
                return -1;
                break;        
        }
        prev = s[i];
    }
    return  count;
}
