import datetime
class User:
    def __init__(self,name: str,contact_info: str,conversations: list):
        self.setName(name)
        self.setContactInfo(contact_info)
        self.setConversations(conversations)


    def setName(self,name):
        if isinstance(name,str) and name != "":
            self.__name = name
        else:
            print("Invalid name")


    def getName(self):
        return self.__name


    def setContactInfo(self,info):
        if isinstance(info,str) and info != "":
            self.__contact_info = info
        else:
            print("Contact info is not valid")


    def getContactInfo(self):
        return self.__contact_info        
    

    def setConversations(self,conversation):
        if isinstance(conversation,list) and len(conversation) != 0:
            self.__conversations = conversation

    def getConversations(self):
        return self.__conversations
    

    def create_conversation(self, user: 'User') -> 'Conversation':
        conversation = Conversation([self,user],[self.__conversations,user.__conversations])
        self.__conversations.append(conversation)
        user.__conversations.append(conversation)
        return conversation
    
    
    def send_message(self, message: 'Message', conversation: 'Conversation') -> None:
        conversation.add_message(message)


    def receive_message(self, message: 'Message') -> None:
        return message
    

    def manage_settings(self) -> None:
        pass


    def get_conversations(self) -> list['Conversation']:
        return self.get_conversations()






class Conversation:
    def __init__(self,participants: list['User'],message_history: list['Message'] ) -> None:
        self.setParticipants(participants)
        self.setMessageHistory(message_history)


    def setParticipants(self,people):
        if isinstance(people,list) and len(people) != 0:
            self.__participants = people
        else:
            print("Invalid input of participants")


    def getParticipants(self):
        return self.__participants
    

    def setMessageHistory(self,history):
        if isinstance(history,list) and len(history) != 0:
            self.__message_history = history
        else:
            print("Invalid history input")


    def getMessageHistory(self):
        return self.__message_history
    

    def add_message(self, message: 'Message') -> None:
        self.__message_history.append(message)

    
    def add_user(self, user: 'User') -> None:
        self.__participants.append(user)

    
    def get_messages(self) -> list['Message']:
        return self.__message_history
    



from abc import abstractmethod

class Message:
    def __init__(self,sender: 'User',conversation: 'Conversation', timestamp: datetime ):
        self.setSender(sender)
        self.setConversation(conversation)
        self.settimestamp(timestamp)


    def setSender(self,sender):
        if isinstance(sender,'User'):
            self.__sender = sender
        else:
            print("Invalid sender")
        

    def getSender(self):
        return self.__sender
    

    def setConversation(self,conversation):
        if isinstance(conversation,'Conversation'):
            self.__conversation = conversation
        else:
            print("Invalid conversation input")
    

    def getConversation(self):
        return self.__conversation
    

    def setTimestamp(self,time):
        if isinstance(time,datetime):
            self.__timestamp = time
        else:
            print("Invald time")

    
    def getTimestamp(self):
        return self.__timestamp
    

    @abstractmethod
    def display_content(self) -> None:
        ...

    @abstractmethod
    def get_message_type(self) -> str:
        ...
