from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup


class Platform(ABC):
    def __init__(self) -> None:
        self.name = "none"
        self.identifier = "none";

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_identifier(self, identifier):
        self.identifier = identifier
    
    def get_identifier(self):
        return self.identifier

    @abstractmethod
    def get_total_solved_problems(self, username):
        pass


class LeetCode(Platform):
    def __init__(self) -> None:
        super().__init__()
        self.set_name("LeetCode");
        self.set_identifier("user name")

    def get_total_solved_problems(self, username):
        url = "https://leetcode.com/graphql"
        query = """
        query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
                submitStats {
                    acSubmissionNum {
                        count
                    }
                }
            }
        }
        """
        variables = {"username": f"{username}"}
        response = requests.post(url, json={'query': query, 'variables': variables})
        user_info = response.json()
        return int(user_info['data']['matchedUser']['submitStats']['acSubmissionNum'][0]['count'])


class CodeForces(Platform):
    def __init__(self) -> None:
        super().__init__()
        self.set_name("Code Forces");
        self.set_identifier("user name")    

    def get_total_solved_problems(self, username):
        page_url = f"https://codeforces.com/profile/{username}"
        page_data = requests.get(page_url)

        soup = BeautifulSoup(page_data.content, 'lxml')
        soup_content = soup.find('div', {'class': '_UserActivityFrame_counterValue'}).text
        solved_problems = int(soup_content.split(' ')[0])
        return solved_problems


class CodeChef(Platform):
    def __init__(self) -> None:
        super().__init__()
        self.set_name("Code Chef");
        self.set_identifier("user name")
    

    def get_total_solved_problems(self, username):
        page_url = f"https://www.codechef.com/users/{username}"
        page_data = requests.get(page_url)

        soup = BeautifulSoup(page_data.content, 'lxml')
        soup_content = soup.find('section', {'class': 'rating-data-section problems-solved'}).find_all('h3')[3]
        solved_problems = int(soup_content.text.split(' ')[-1])
        return solved_problems

class AtCoder(Platform):
    def __init__(self) -> None:
        super().__init__()
        self.set_name("At Coder")
        self.set_identifier("user name")    

    def get_total_solved_problems(self, username):
        page_url = f"https://kenkoooo.com/atcoder/atcoder-api/v3/user/ac_rank?user={username}"
        page_data = requests.get(page_url).json()
        return int(page_data['count'])


class UVA(Platform):
    def __init__(self) -> None:
        super().__init__()
        self.set_name("UVA");
        self.set_identifier("user id")
        # self.userid = "1483780"
    
    def get_total_solved_problems(self, userid):
        url = f"https://uhunt.onlinejudge.org/api/ranklist/{userid}/1/1"
        user_data = requests.get(url).json()[0]
        return user_data['ac']

class SPOJ(Platform):
    def __init__(self) -> None:
        super().__init__()
        self.set_name("SPOJ")
        self.set_identifier("user name")
        # self.username = "islam_imad"
    

    def get_total_solved_problems(self, username):
        page_url = f"https://www.spoj.com/users/{username}/"
        page_data = requests.get(page_url)

        soup = BeautifulSoup(page_data.content, 'lxml')
        soup_content = soup.find('dl', {'class': 'profile-info-data-stats'})
        soup_content = soup_content.find('dd').text

        return int(soup_content)


class PlatformFactory:
    @staticmethod
    def get_platform(platform_name):
        if platform_name == "LeetCode":
            return LeetCode()
        elif platform_name == "CodeForces":
            return CodeForces()
        elif platform_name == "CodeChef":
            return CodeChef()
        elif platform_name == "AtCoder":
            return AtCoder()
        elif platform_name == "UVA":
            return UVA()
        elif platform_name == "SPOJ":
            return SPOJ()
        return None
