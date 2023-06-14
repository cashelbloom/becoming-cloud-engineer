'''
eVoting System:
    Functionalities to Build:
        1. List the registered voters for selection
            Each voter name is tagged with an alphabet
                For example: Voter 'Rama' is shown as a : Rama (without the quotes surrounding them)

        2. Validate voter selection
            Accept a character as input from the user and validate if the character entered is one of the available
            characters for any of the registered voters.
            if valid character entered, display a prompt for entering voter id
            If no matching character found for any voter name, then present the same display to enter a valid selection
            After 3 attempts, the application should say "a sorry message" and end the execution of the program.
        3. Validate voter id match with voter name selection
            (which should be only natural numbers - that is any positive whole number)
            if matching voter name is found for the given number
                proceed to the next part of the flow
            else provide 2 more attempts
            If 3 attempts failed to match the voter name, then the program should end with a message.
        4. Present a ballot paper to the authenticated voter.
            The ballot paper should have, for each candidate:
                name, party name, symbol
                Here are the candidates and their details:
                    1. John David - People Party - Peacock
                    2. Jay Sam  - Labour Party - Donkey
                    3. Cathy Joe - Liberal Party - Book
                    4. Ray Jenson - Independent - Plane
        5. Prompt the user to enter the name of the symbol for their voting choice.
            Once received the input for the symbol, validate the symbol entry
            if valid entry, add a vote to the candidate chosen.
            Each vote should be saved to a JSON file that contains:
                the candidate name as the key and the number of votes as the value
                The name of the file is votes_tally.json
        6. When All votes are cast, then declare the results, showing the votes polled for each candidate.

        Additional Considerations if you are comfortable to program:
        Since in the real world voting procedure, there will be original list of all the eligible voters to cast
        their vote in a voting location. As a voter authenticates to the polling official, then a record is made
        to account for that voter completing their voting to prevent multiple voting by a voter. You can consider
        another dictionary consisting of voter id and voter name and can label this dictionary as completed_voters.
        There can be another dictionary to show the current outstanding voters that haven't completed their voting.
        This dictionary is the difference between the original voters list dictionary and the completed voters dictionary.
        So, your program should be looping until there is no element left in the current outstanding voters dictionary.


'''