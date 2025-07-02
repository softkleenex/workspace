# 이름이 main 폴더 안에 여러가지 파일과 폴더가 존재한다.

# main
#  ├─ FolderA
#  │    ├─ File1
#  │    └─ File2
#  └─ FolderB
#        ├─ FolderC
#        ├─ File1
#        └─ File3
# 위 구조는 main 폴더의 하위 구조를 계층적으로 표시한 것이다. FolderA, FolderB, FolderC는 폴더이고 File1, File2, File3은 파일이다. 파일 이름이 같은 경우는 동일한 파일이다.

# 한 폴더 안에는 같은 이름의 파일이 두 개 이상 존재할 수 없다.

# main 하위 디렉토리에 같은 이름의 폴더가 두 개 이상 존재할 수 없다.

# 폴더 정리를 하기 위해 main 폴더 하위에 있는 파일들을 확인하려고 한다.

# 주어지는 쿼리에 대해 폴더와 파일의 정보를 알려주는 프로그램을 만들어보자.

# 입력
# 첫 번째 줄에는 main 폴더 하위에 있는 폴더의 총 개수 $N$과 파일의 총 개수 $M$이 공백으로 구분되어 주어진다.

# 두 번째 줄부터 $N + M + 1$ 번째까지 상위 폴더의 이름 $P$, 폴더 또는 파일의 이름 $F$, 폴더인지 아닌지 알려주는 $C$가 공백으로 구분되어 주어진다.

#  $C$의 값은 $F$가 폴더라면 1, 파일이라면 0으로 주어진다.

#  $N + M + 2$ 번째 줄에는 쿼리의 개수 $Q$가 주어진다.

# 그 다음줄부터 $Q$개의 쿼리가 주어진다. 쿼리마다 main부터 폴더의 경로 정보가 들어온다. 예를 들어 main 폴더 안에 FolderB에 대한 쿼리가 들어온다면, FolderB의 경로인 main/FolderB로 주어진다. 반드시 폴더가 존재하는 경로로 주어짐을 보장한다.

# 출력
# 쿼리 순서대로 한 줄씩 폴더 하위에 있는 파일의 종류의 개수와 파일의 총 개수를 출력한다.

# 파일의 종류의 개수는 같은 파일이 여러개 있을 경우 하나로 계산한다. 파일의 총 개수는 같은 파일이 있더라도 하나로 계산하지 않는다.

# 예를 들어 이름이 File1 파일이 5개가 있을 경우 파일의 종류는 1 가지이고 파일의 총 개수는 5개이다.

# 제한
#  $1 \le N \le 1,000$ 
#  $1 \le M \le 1,000$ 
#  $1 \le |P| \le 10$ 
#  $1 \le |F| \le 10$ 
#  $0 \le C \le 1$ 
#  $1 \le Q \le 1,000$ 
#  $P$와 $F$는 영어 알파벳 대소문자, 숫자로만 이루어져 있다.
# 예제 입력 1 
# 3 4
# main FolderA 1
# main FolderB 1
# FolderA File1 0
# FolderA File2 0
# FolderB FolderC 1
# FolderB File1 0
# FolderB File3 0
# 4
# main
# main/FolderA
# main/FolderB
# main/FolderB/FolderC
# 예제 출력 1 
# 3 4
# 2 2
# 2 2
# 0 0
# main 폴더 하위에는 FolderA 폴더 하위에 있는 File1, File2, FolderB 폴더 하위에 있는 File1, File3이 있다.

# 파일의 종류는 File1, File2, File3 총 3가지이고, 파일의 총 개수는 File1, File2, File1, File3 총 4개이다.

# main/FolderB/FolderC 폴더 하위에 있는 파일은 아무것도 없기 때문에 파일의 종류와 파일의 총 개수가 모두 0이다.

# 예제 입력 2 
# 4 1
# main FolderA 1
# FolderA FolderB 1
# FolderB FolderC 1
# FolderC FolderD 1
# FolderD File1 0
# 3
# main
# main/FolderA
# main/FolderA/FolderB/FolderC/FolderD
# 예제 출력 2 
# 1 1
# 1 1
# 1 1





def search1(filelist, start, typeset):  # 파일의 종류 계산

    selected = []
    for i in filelist:
        if i.split('\\')[0] == i:
            selected.append(i)

    print(selected)
    #selected 는 start 의 하위것들


    for i in filelist[start]:
        if i not in filelist:  # 파일
            typeset.add(i)
        else:  # 폴더
            search1(filelist, i, typeset)
    return typeset




def search2(filelist, start):  # 파일의 총 개수 계산
    n = 0
    for i in filelist[start]:
        if i not in filelist:  # 파일
            n += 1
        else:  # 폴더
            n += search2(filelist, i)
    return n





fols, files = map(int, input().split())
filelist = dict(main = 1)


for i in range(fols + files):
    start, name, fol = input().split()#fol 이 1 이면 폴더 0 이면 파일
   

    filelist[start + '\\' + name] =  fol




print(*filelist.items(), sep = '\n')



q = int(input())

for i in range(q):
    start = input().strip().split('/')
  

    start =  start[-1]


    a, b = len(search1(filelist, start, set())), search2(filelist, start)
    print(a, b)
