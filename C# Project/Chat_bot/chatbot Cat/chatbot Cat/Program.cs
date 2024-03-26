using System;
using System.Collections.Generic;
class CatChatbot
{
    private Dictionary<string, Func<string, string>> _response;
    public CatChatbot()
    {
        _response = new Dictionary<string, Func<string, string>>
        {
            {"Hi, Would you like to talk about cats?: ", RespondToQuestion
            { }
        };
    }

    public void StartConversation()
    {
        Console.WriteLine("Hello!! Welcome~~    . Type 'exit' to end the conversation");
        RespondToUserInput();
    }

    private void (var question in _responses)

}

{ "Hi!, Do you like cats?: ", RespondToCat },
            "Would you like to talk about cats?: " },
            { "What is your name?: ", "Do you have cats?: " },
            { "How many cats do you have: ", "What is your cat's name?: " },
            { "Did you know that a house cat's genome is 95.6% tiger?: ", "Did you know that Isaac Newton invented the cat door?: " },