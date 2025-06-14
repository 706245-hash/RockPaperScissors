import random
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

class RockPaperScissors:
    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        self.rounds_played = 0
        self.ascii_art = {
            'rock': f"""{Fore.RED}
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """,
            'paper': f"""{Fore.BLUE}
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """,
            'scissors': f"""{Fore.GREEN}
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """
        }
        
    def display_welcome(self):
        print(f"""{Fore.YELLOW}
        {Style.BRIGHT}Welcome to {Fore.CYAN}Rock{Fore.MAGENTA} Paper{Fore.GREEN} Scissors{Fore.YELLOW}!
        {Fore.WHITE}---------------------------------
        {Style.RESET_ALL}Rules:
        {Fore.RED}■ Rock {Fore.WHITE}crushes {Fore.GREEN}Scissors
        {Fore.GREEN}■ Scissors {Fore.WHITE}cut {Fore.BLUE}Paper
        {Fore.BLUE}■ Paper {Fore.WHITE}covers {Fore.RED}Rock
        {Fore.WHITE}
        Commands:
        {Fore.CYAN}■ Type 'rock', 'paper', or 'scissors' to play
        {Fore.MAGENTA}■ Type 'stats' to see current statistics
        {Fore.GREEN}■ Type 'best' for best of three mode
        {Fore.YELLOW}■ Type 'quit' to exit the game
        """)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            return 'user'
        else:
            return 'computer'
    
    def display_choices(self, user_choice, computer_choice):
        print(f"\n{Fore.CYAN}Your choice:{Style.RESET_ALL}")
        print(self.ascii_art[user_choice])
        
        print(f"{Fore.MAGENTA}Computer's choice:{Style.RESET_ALL}")
        print(self.ascii_art[computer_choice])
    
    def display_result(self, result):
        if result == 'tie':
            print(f"\n{Back.YELLOW}{Fore.BLACK} IT'S A TIE! {Style.RESET_ALL}")
        elif result == 'user':
            print(f"\n{Back.GREEN}{Fore.BLACK} YOU WIN THIS ROUND! {Style.RESET_ALL}")
        else:
            print(f"\n{Back.RED}{Fore.BLACK} COMPUTER WINS THIS ROUND! {Style.RESET_ALL}")
    
    def display_stats(self):
        print(f"\n{Back.CYAN}{Fore.BLACK}{Style.BRIGHT}=== GAME STATISTICS ==={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Rounds Played: {Fore.WHITE}{self.rounds_played}")
        print(f"{Fore.GREEN}Your Wins: {Fore.WHITE}{self.user_score}")
        print(f"{Fore.RED}Computer Wins: {Fore.WHITE}{self.computer_score}")
        print(f"{Fore.BLUE}Ties: {Fore.WHITE}{self.ties}")
        
    def play_round(self):
        while True:
            user_choice = input(f"\n{Fore.YELLOW}Choose {Fore.RED}rock{Fore.YELLOW}, {Fore.BLUE}paper{Fore.YELLOW}, {Fore.GREEN}scissors{Fore.YELLOW} (or 'stats', 'quit'): {Style.RESET_ALL}").lower()
            
            if user_choice == 'quit':
                return False
            elif user_choice == 'stats':
                self.display_stats()
                continue
            elif user_choice not in self.options:
                print(f"{Fore.RED}Invalid choice. Please try again.")
                continue
                
            computer_choice = random.choice(self.options)
            result = self.determine_winner(user_choice, computer_choice)
            
            self.rounds_played += 1
            if result == 'user':
                self.user_score += 1
            elif result == 'computer':
                self.computer_score += 1
            else:
                self.ties += 1
                
            self.display_choices(user_choice, computer_choice)
            self.display_result(result)
            return True
    
    def play_best_of_three(self):
        print(f"\n{Back.MAGENTA}{Fore.BLACK}{Style.BRIGHT}=== BEST OF THREE MODE ==={Style.RESET_ALL}")
        original_scores = (self.user_score, self.computer_score, self.ties)
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        
        while max(self.user_score, self.computer_score) < 2 and (self.user_score + self.computer_score + self.ties) < 5:
            if not self.play_round():
                self.user_score, self.computer_score, self.ties = original_scores
                return
            
        print(f"\n{Back.CYAN}{Fore.BLACK}{Style.BRIGHT}=== FINAL RESULT ==={Style.RESET_ALL}")
        if self.user_score > self.computer_score:
            print(f"{Fore.GREEN}{Style.BRIGHT}You won the best of three! 🎉")
        elif self.computer_score > self.user_score:
            print(f"{Fore.RED}{Style.BRIGHT}Computer won the best of three! 💻")
        else:
            print(f"{Fore.YELLOW}{Style.BRIGHT}It's a draw in the best of three! 🤝")
        
        self.display_stats()
        self.user_score, self.computer_score, self.ties = original_scores
    
    def start_game(self):
        self.display_welcome()
        
        while True:
            print(f"\n{Style.BRIGHT}{Fore.YELLOW}Main Menu{Style.RESET_ALL}")
            print(f"{Fore.CYAN}1. {Fore.WHITE}Play single round")
            print(f"{Fore.MAGENTA}2. {Fore.WHITE}Best of three")
            print(f"{Fore.RED}3. {Fore.WHITE}Quit")
            
            choice = input(f"{Fore.YELLOW}Enter your choice (1-3): {Style.RESET_ALL}")
            
            if choice == '1':
                self.play_round()
            elif choice == '2':
                self.play_best_of_three()
            elif choice == '3':
                print(f"\n{Fore.GREEN}Thanks for playing!{Style.RESET_ALL}")
                self.display_stats()
                break
            else:
                print(f"{Fore.RED}Invalid choice. Please enter 1, 2, or 3.")

# Start the game
if __name__ == "__main__":
    game = RockPaperScissors()
    game.start_game()