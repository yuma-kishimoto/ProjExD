import random 
import datetime

num_of_alphabet = 26
num_of_all_chars = 10
num_of_abs_chars = 2 #欠損文字
num_roop = 2

def toi(alphabet):
    all_chars = random.sample(alphabet,num_of_all_chars)
    print("対象文字")
    for c in all_chars:
        print(c,end="")
    print()



    abs_chars = random.sample(all_chars, num_of_abs_chars)
    print("欠損文字")
    for c in abs_chars:
        print(c,end="")
    print()
    


    print("表示文字")
    for c in all_chars:
        if c not in abs_chars:
            print(c,end="")
        print()

        return abs_chars

def kaitou(abs_chars):
    num = int(input("欠損文字いくつ?"))
    if num != num_of_abs_chars:
        print("不正解")
    else:
        print("正解。欠損文字入力してくれ")
        for i in range(num):
            ans = input(f"{i + 1}つめの文字いれろ:")
            if ans not in abs_chars:
                print("不正解")
                return False
            else:
                abs_chars.remove(ans)
        
        print("全部正解じゃ")
        return True

if __name__ == "__main__":
    st = datetime.time()
    alphabet=[chr(i+65) for i in range(num_of_alphabet)]
    print(alphabet)
    for j in range(num_roop):
         abs_chars = toi(alphabet)
         ret = kaitou(abs_chars)
         if ret:
            break
         else:
            print("-"*20)
    
    ed = datetime.time()
    print(f"所要時間:{(ed-st):.2f}秒")
