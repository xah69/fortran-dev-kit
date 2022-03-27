program odd_even

 implicit none
 
 !var
 integer :: n1,calc
 character(10) :: s1 
 logical :: t,f

 t = .true.
 f = .false.
 
 print *, "[welcome to odd or even finder]"
 print *, " "
 
 do while (t)
  
  print *, "Enter the number -->"
  read(*,*) n1
  
  if (n1 == 0) then
   print *, "[exiting]"
   exit
  end if 
  
  calc = mod(n1,2)
  
  if (calc == 0) then
   print *, n1," is even"
  else
   print *, n1," is odd"
  end if  
 
 end do
end program odd_even
