#include <iostream>
#include <fstream>
#include <string>

int main () 
{
   std::string mystring;
   std::ifstream myfile ("input.txt");

   if ( myfile.is_open() )  // always check whether the file is open
   {
      char mychar;
      int counter;
      while ( myfile ) 
      {
         mychar = myfile.get();
         counter = myfile.tellg();

         std::cout << mychar;
         std::cout << "[" << counter << "]";

         //this prints it like this:
         //  000011010001:13
         //  000001110100:26
         //  111100101010:39

         // if (mychar != '\n')
         //    std::cout << mychar;
         // else
         //    std::cout << ":" << counter << "\n" ;
      }
   }
}
