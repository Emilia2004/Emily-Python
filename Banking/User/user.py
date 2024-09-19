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
    



from abc import ABC,abstractmethod

class Message(ABC):
    def __init__(self,sender: 'User',conversation: 'Conversation', timestamp: datetime ):
        self.setSender(sender)
        self.setConversation(conversation)
        self.setTimestamp(timestamp)


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




class TextMessage(Message):
    def __init__(self,sender: 'User',conversation: 'Conversation', timestamp: datetime,content:str):
        super().__init__(sender,conversation, timestamp)
        self.setContent(content)


    def setContent(self,content):
        if isinstance(content,str) and content != "":
            self.__content = content
        else:
            print("Invalid content")
        

    def getContent(self):
        return self.__content
    

    def display_content(self) -> None:
        return self.__conversation


    def get_message_type(self) -> str:
        if self.__content.isdigit():
            return int
        return str
    


class MultimediaMessage(Message):
    def __init__(self,sender: 'User',conversation: 'Conversation', timestamp: datetime,file_path: str,media_type: str):
        super().__init__(sender,conversation, timestamp)
        self.setFilePath(file_path)
        self.setMediaType(media_type)


    def setFilePath(self,path):
        if isinstance(path,str) and path != "":
            self.__file_path = path
        else:
            print("Invalid path")
            

    def getFilePath(self):
        return self.__file_path
        

    def setMediaType(self,type):
        if isinstance(type,str):
            self.__media_type = type
        else:
            print("Invalid type")

            
    def getMediaType(self):
        return self.__media_type
        

    def display_content(self) -> None:
        print(self.__conversation)


    def get_message_type(self) -> str:
        return self.__media_type
        


class MessagingManager(ABC):
    @abstractmethod
    def send_message(self, message: 'Message') -> None:
        ...

    @abstractmethod
    def receive_message(self, message: 'Message') -> None:
        ...

    @abstractmethod
    def view_conversation_history(self, conversation: 'Conversation') -> list['Message']:
        ...




    


     
