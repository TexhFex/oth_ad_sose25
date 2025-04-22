import math

def f(a):
 for i in range(len(a)//2-1,-1,-1):
  h(a,len(a),i)
  print_heap(a)
 for j in range(len(a)-1,0,-1):
  a[0],a[j]=a[j],a[0]
  print(a)
  h(a,j,0)

def h(a,n,i):
 l=2*i+1; r=2*i+2
 if l<n and a[l]>a[i]: i=l
 if r<n and a[r]>a[i]: i=r
 if i!= (i):
  a[i],a[(i)] = a[(i)],a[i]
  h(a,n,i)

def print_heap(a):
 if not a: return
 lv=int(math.log2(len(a)))+1
 for d in range(lv):print(' '*(lv-d)+','.join(str(x)for x in a[2**d-1:2**(d+1)-1]))

def m(a,d=0):
 print('  '*d+str(a))
 if len(a)<2: return a
 m1=m(a[:len(a)//2],d+1)
 m2=m(a[len(a)//2:],d+1)
 i=j=0;r=[]
 while i<len(m1)and j<len(m2):
  if m1[i]<m2[j]:r.append(m1[i]);i+=1
  else:r.append(m2[j]);j+=1
 r+=m1[i:]+m2[j:]
 print('  '*d+str(r))
 return r

a=[-5,13,-32,7,-3,17,23,12,-35,19]
print(m(a[:]))
f(a[:])
