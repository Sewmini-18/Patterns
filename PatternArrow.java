import java.util.Scanner;

//PatternArrow.java

class PatternArrow
{
    public static void main(String[] args)
    {
       Scanner sc = new Scanner(System.in);
	   System.out.print("Enter Number:(n>1) ");
	   int num = sc.nextInt();
	   System.out.print("Enter Pattern(char): ");
	   char pattern = sc.next().charAt(0);
	   
	   PrintPattern ppt = new PrintPattern(num,pattern);		   
			   
}
}

class PrintPattern{
	
	PrintPattern(int num, char pattern){
		int i,j,space;
	int r=num+(num-1);
		for(i=1; i<= num; i++){
		   System.out.print(" ");
		   for(space=1; space<=(num-i);space++)
		   {
			System.out.print(" ");   
			   
		   }
			for(j=1; j<=(i+i-1);j++){
			System.out.print(pattern);   
			   
		   }
		   System.out.println(); 
	}
	
	   
	   
		for(i=0;i<r;i++){
		   System.out.print(" ");
		   if(num<4){
		   for(space=1; space<=(r/2);space++)
		   {
			System.out.print(" ");   
		   }   
		   System.out.print(pattern);
		   System.out.println("");
		   }
		   else{
		   if(num%2==1){
			   for(space=1; space<=(num/2);space++)
		   {
			System.out.print(" ");   
		   }
			for(j=1; j<=num;j++)
		   {
			System.out.print(pattern);   
		   }   
		   
		   System.out.println("");
		   }
		   else{
			   for(space=1; space<=(num/2);space++)
		   {
			System.out.print(" ");   
		   }
			for(j=1; j<=num-1;j++)
		   {
			System.out.print(pattern);   
		   }   
		   
		   System.out.println("");
		   }
		   }		   
	   }
		
	}
}

