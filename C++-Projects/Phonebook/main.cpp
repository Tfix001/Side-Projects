#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int menu();
void displayBook(fstream&);
void addContact(fstream&);
void searchContacts(fstream&);
void updateContact(fstream&);
void deleteContact(fstream&);

int main(){
  fstream inF;
  string userSting;
  inF.open("Phonebook.txt");
  if(inF.is_open()){
    int choice = menu();
    while(choice != 5){
      switch(choice){
        case 1:
          cout << "ADD CONTACT" << endl;
          addContact(inF);
          choice = menu();
          break;
        case 2:
          cout << "SEARCH CONTACTS" << endl;
          cout << "\"Manual\" Search or \"Automatic\"?" << endl;
          cin >> userSting;
          if(userSting == "Manual"){
            displayBook(inF);
          }
          else if(userSting == "Automatic"){
            searchContacts(inF);
          }
          choice = menu();
          break;
        case 3:
          cout << "UPDATE CONTACT" << endl;
          choice = menu();
          break;
        case 4:
          cout << "DELETE CONTACT" << endl;
          choice = menu();
          break;
        default:
          cout << "Error, choice is none of the above, leaving phonebook" << endl;
          choice = 5;
          break;
      }
    }
    inF.close();
  }
  return 0;
}

int menu(){
  int userChoice;
  cout << "1. Add contact." << endl;
  cout << "2. Search contacts." << endl;
  cout << "3. Update contact." << endl;
  cout << "4. Delete contact." << endl;
  cout << "5. Leave phonebook." << endl;
  cin >> userChoice;
  return userChoice;
}

void displayBook(fstream& file){
  string line;
  while(getline(file, line)){
    cout << line << endl;
  }
  if(file.eof()){
    cout << "End of phonebook reached" << endl;
  }
  else{
    cout << "Encountered some error" << endl;
  }
}

void addContact(fstream& file){
  file.insert(file.begin() + )
}
