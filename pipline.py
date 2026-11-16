from Agents import get_scraped_agent,get_research_agent,crictic_chain , writer_chain
from rich import print


def run_Agent_pipline(topic : str)-> dict:
    
    
    state ={}


    
    #First Agent
    print("-"*50)
    print("Search Agent IS Working. . .")
    print("-"*50)

    
    search_agent = get_research_agent()
    search_result = search_agent.invoke({
        "messages":[("user",f"You have to give recent , relaible and revelant answer according to the {topic}")]
    })

    state["Search_Results"] = search_result["messages"][-1].content
    print("\n Search Result : ",state["Search_Results"])



   
    #Second Agent
    print("-"*50)
    print("Scraped Agent IS Working. . .")                                                       
    print("-"*50)

    scraped_agent = get_scraped_agent()
    scraped_result = scraped_agent.invoke({
        "messages": [("user",
    f"Based on the following search results about '{topic}', "
    f"pick the most relevant URL and scrape it for deeper content.\n\n"
    f"Search Results:\n{state["Search_Results"][:800]}"

    )]
      })
    state["scraped_results"] = scraped_result["messages"][-1].content
    print("\n Scraped Result :",state["scraped_results"])


    #Search Report
    print("-"*50)
    print("Search Prompt")                                                       
    print("-"*50)

    research_combined = ({
        "Result":state["Search_Results"],
        "Detailed": state["scraped_results"]
    })
    
    state["Report"] =  writer_chain.invoke({
        'topic': topic,
        "research": research_combined
    })

    
    print("\n Report :",state["Report"])

    


    #Crictic |Report
    print("-"*50)
    print("Crictic Report")                                                       
    print("-"*50)

    state["Feedback"]=crictic_chain.invoke({
        "report": state["Report"]
    })

    print("\n Feedback/ Conculsion :",state["Feedback"])

    return state


if __name__ =="__main__":

    topic = input("Enter you Search Topic : ")
    run_Agent_pipline(topic)




     
