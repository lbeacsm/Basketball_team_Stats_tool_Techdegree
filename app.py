from constants import PLAYERS
from constants import TEAMS
import copy
players2 = copy.deepcopy(PLAYERS)
teams2 = copy.deepcopy(TEAMS)
cleandata = []
if __name__ == "__main__":
    def basketball_stats():
          def clean_data():
              for players in players2:
                  clean = {}
                  clean['name'] = players['name']
                  clean ['guardians'] = players['guardians']  
                  if players['experience'] == 'YES':
                      clean['experience'] = True 
                  else: 
                      clean['experience'] = False 
                      clean['height'] = int(players['height'].split(' ')[0])
                      cleandata.append(clean)
                      
              return cleandata 
          clean_data()
          
          num_players = len(cleandata) // len(teams2)
          names =[players['name'] for players in players2]
          Panthers = [] 
          Bandits = []
          Warriors = []
          def balance_teams():
              for team in [Panthers , Bandits, Warriors]: 
                  while len(team) < num_players :
                      team.append(names.pop())
                    
          balance_teams()           
            
          print ("BASKETBALL TEAM STATS")
          print ("       --MENU--      ")
          print("Here are your choices:  ")
          print("A) Display team stats") 
          print("B) quit")
          answer = input("Choose your option:   ") 
          while answer.lower() == 'a' :
              print("A) PANTHERS")
              print ("B)BANDITS")
              print("C)WARRIORS")
              option = input("Enter an option:  ") 
              if option.lower()  == 'a':
                  print ("PANTHER STATS")
                  print("--------------------")
                  print(" Total number of players is : {} " .format(num_players))
                  print("Players on team: {}" .format(','.join(Panthers)))

              elif option.lower() == 'b': 
                  print ("BANDITS STATS")
                  print("--------------------")
                  print(" Total number of players: {} " .format(num_players))
                  print("Players on team: {}" .format(','.join(Bandits)))

              elif option.lower() == 'c':
                  print ("WARRIOR STATS")
                  print("--------------------")
                  print(" Total number of players: {} " .format(num_players))
                  print("Players on team: {}" .format(','.join(Warriors)))
              else: 
                  print("Please write one of the options (A,B OR C)")
              ask = input("Press Enter to continue...")
              if ask.lower() != 'enter':
                  print("end")
                  break
              else:
                  continue 
          print("Bye...")
      
      
    basketball_stats()  

    
  
