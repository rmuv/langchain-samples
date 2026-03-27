import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

def main():
    print("Hello from langchain-samples!")
    print(os.environ.get("OPENAI_API_KEY"))
    information = """
    The Grand Canyon[a] is a steep-sided canyon carved by the Colorado River in Arizona, United States. The Grand Canyon is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of over a mile (6,093 feet or 1,857 meters).[6]: 902 

    The canyon and adjacent rim are contained within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon–Parashant National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation and the Navajo Nation. President Theodore Roosevelt was a major proponent of the preservation of the Grand Canyon area and visited it on numerous occasions to hunt and enjoy the scenery.

    Nearly two billion years of Earth's geological history have been exposed as the Colorado River and its tributaries cut their channels through layer after layer of rock while the Colorado Plateau was uplifted.[7][8] While some aspects about the history of incision of the canyon are debated by geologists,[7][9] several recent studies support the hypothesis that the Colorado River established its course through the area about 5 to 6 million years ago.[1][7][10][11] Since that time, the Colorado River has driven the down-cutting of the tributaries and retreat of the cliffs, simultaneously deepening and widening the canyon.

    For thousands of years, the area has been continuously inhabited by Native Americans, who built settlements within the canyon and its many caves. The Pueblo people considered the Grand Canyon a holy site, and made pilgrimages to it.[12] The first European known to have viewed the Grand Canyon was García López de Cárdenas from Spain, who arrived in 1540.

    """

    summary_template = """
    Given the following information, Provide 2 facts about grand canyon:
    {information}
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})

    print(response)

if __name__ == "__main__":
    main()
