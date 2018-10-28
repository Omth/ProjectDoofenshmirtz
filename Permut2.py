while (1):
    terms = int(input())

    if (terms ==0):
        break
    else:
        arr = list(map(int,input().split(' ')))

        for i in range (1,terms+1):

            k = arr[i-1]

            try:
                req = arr[k-1]
            except IndexError:
                print ('not ambiguous')
                break
            else:
                if (i==req):
                    continue
                elif(i!=req):
                    print ('not ambiguous')
                    break
        else:
            print ('ambiguous')
