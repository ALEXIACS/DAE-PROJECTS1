using System;
using System.Collections.Generic;

class ChatBotCat
{
 private string _userName;

 private string _AskName = "Hello!! My name is Meoww, What is your name??: ";
 private string _LikeCats = "Do you like cats?: "
 private string _CatTalk = "Would you like to talk about cats?: "
 private string _CuriousFact = "Do you have a cat?: "
 private string _CatNumb = "How many cats do you have?: "

 public ChatBotCat
 //Start of the interrogatory

private string AskForName()
{
    Console.WriteLine(_AskName);
    Console.Write("User: ");
    return Console.ReadLine();
}
    public void ConvStart()
    {
        Console.Writeline("You entered the chat... If you want to end the conversation type 'exit' ")
        _userName = AskName(); 
        Console.WriteLine($"Meoww: Nice to meet you, {_userName});

        Ask
    }

}