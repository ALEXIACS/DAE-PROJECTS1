using System;
using System.Collections.Generic;

class CatChatbot
{
    private Dictionary<string, string> _responses;
    private List<string> _questions;

    public CatChatbot()
    {
        _responses = new Dictionary<string, string>
        {
            {"Hi, what is your name?: ", "Would you like to talk about cats?: "}
            {"Do you have cats?: ", "Would you like to know some interesting facts about cats??: "}
            {"How many cats do you have??: ", "That's awesome!! What are your cats' names?: "}
            {"Did you know that a house cat's genome is 95.6% tiger?"}
        };
    }

    public void StartConversation()
    {
        Console.Writeline("Hallo, welcome!!, Trying to end the conversation? Type exit :( ");

        foreach (var question in _questions)
        {
            AskQuestion(question);
        }
    }








    private void AskQuestion(string question)
    {
        Console.Write(question);
        string userInput = Console.ReadLine();

        if (userInput.ToLower() == "exit")
        return;

        string response = GetResponse(userInput);
        Console.WriteLine(response);
    }

private string GetResponse(string userInput)
{
    if (_responses.ContainsKey(userInput))
    {
        return _responses[userInput];
    }
    else
    {
        return ""
    }
}
}