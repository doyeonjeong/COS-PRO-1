# 3회 - 문제 10. 밥먹고 머리자르고

"""
미용실과 레스토랑이 예약을 받는 기준은 다음과 같습니다.

* 미용실
  * 인원수가 1명인 경우에만 예약받습니다.
  * 다른 손님과 예약 시간이 겹칠 수 없습니다.

* 레스토랑
  * 인원수가 2명 이상 8명 이하인 경우에만 예약받습니다.
  * 최대 두 팀까지 예약 시간이 겹칠 수 있습니다.

두 가게에서 예약을 받은 횟수를 계산하기 위해 다음과 같이 Customer, Shop, HairShop, Restaurant 클래스를 작성했습니다.

  ![shop1_cpp.png](https://grepp-programmers.s3.amazonaws.com/files/ybm/99be08777d/c0d50c3c-f5c0-4932-a63e-80aab959d75d.png)

* Customer:
  * Customer : 고객을 나타내는 클래스입니다.
  * id : 고객 식별 번호를 나타냅니다.
  * time : 고객이 신청한 예약 시간을 나타냅니다.
  * num_of_people : 예약 인원 수를 나타냅니다.

* Shop :
  *  Shop : 가게를 나타내는 클래스입니다.
  * reserve_list : 가게에 예약한 고객 리스트입니다.
  * reserve : 고객을 매개변수로 받아, 예약 고객 리스트에 추가 후 true를 return합니다.

* HairShop :
  * HairShop : 미용실을 나타내는 클래스이며, Shop을 상속합니다.
  * reserve : 고객을 매개변수로 받아, 미용실의 예약 기준에 맞는지 검사 합니다. 예약을 받았다면 예약 고객 리스트에 추가 후 true를 return하고, 그렇지 않으면 false를 return 합니다.

* Restaurant :
  * Restaurant는 레스토랑을 나타내는 클래스이며, Shop을 상속합니다.
  * reserve : 고객을 매개변수로 받아, 레스토랑의 예약 기준에 맞는지 검사 합니다. 예약을 받았다면 예약 고객 리스트에 추가 후 true를 return하고, 그렇지 않으면 false를 return 합니다.

예약을 원하는 고객 정보가 담긴 리스트 customers와 shops가 매개변수로 주어질 때, 두 가게에서 예약받은 횟수를 return 하도록 solution 함수를 작성하려고 합니다. 위 클래스 구조를 참고하여 주어진 코드의 빈칸을 적절히 채워 전체 코드를 완성해주세요.

---
#####매개변수 설명
예약을 원하는 고객 정보가 담긴 리스트 customers와 shops가 solution 함수의 매개변수로 주어집니다.
* customers의 길이와 shops의 길이는 항상 같습니다.
* customers의 각 원소에는 고객 정보가 [고객 ID, 예약 시간, 예약 인원수] 순으로 들어있습니다.
  * 고객 ID는 1 이상 10,000 이하인 자연수입니다.
  * 예약 시간은 0 이상 23 이하인 정수입니다.
  * 예약 인원수는 1 이상 10 이하인 자연수입니다.
  * 고객 ID는 중복해서 주어지지 않습니다.
* customers에는 고객이 예약을 신청한 순서대로 들어있습니다. 
* shops는 각 고객이 예약할 가게를 나타내며, "hairshop" 또는 "restaurant" 로만 구성되어 있습니다.
* i 번째 고객이 예약할 가게는 shops[i] 입니다.
* 예약을 신청한 고객의 수는 1 이상 10 이하입니다.

---
#####return 값 설명
두 가게에서 예약받은 횟수를 return 해주세요.

---
#####예시

| customers                                                               | shops                                                            | return |
|-------------------------------------------------------------------------|------------------------------------------------------------------|--------|
| [[1000, 2, 1], [2000, 2, 4], [1234, 5, 1], [4321, 2, 1], [1111, 3, 10]] | ["hairshop", "restaurant", "hairshop", "hairshop", "restaurant"] | 3      |

#####예시 설명

고객별 예약 정보는 다음과 같습니다.

| ID   | 예약 시간 | 인원수 | 가게       |
|------|-----------|--------|------------|
| 1000 | 2         | 1      | hairshop   |
| 2000 | 2         | 4      | restaurant |
| 1234 | 5         | 1      | hairshop   |
| 4321 | 2         | 1      | hairshop   |
| 1111 | 3         | 10     | restaurant |

* 첫 번째 고객은 미용실에서 예약받습니다.
* 두 번째 고객은 레스토랑에서 예약받습니다.
* 세 번째 고객은 미용실에서 예약받습니다.
* 네 번째 고객은 예약받지 않습니다. 2시에 미용실을 먼저 예약한 손님이 있기 때문입니다.
* 다섯 번째 고객은 예약받지 않습니다. 레스토랑에 한 번에 예약 가능한 인원수는 2명 이상 8명 이하입니다.
"""


# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class Customer:
    def __init__(self, id, time, num_of_people):
        self.id = id
        self.time = time
        self.num_of_people = num_of_people


class Shop:
    def __init__(self):
        self.reserve_list = []

    def reserve(self, customer):
        self.reserve_list.append(customer)
        return True


class HairShop(Shop):
    def __init__(self):
        super().__init__()

    def reserve(self, customer):
        if customer.num_of_people != 1:
            return False
        for r in self.reserve_list:
            if customer.time == r.time:
                return False
        self.reserve_list.append(customer)
        return True


class Restaurant(Shop):
    def __init__(self):
        super().__init__()

    def reserve(self, customer):
        if customer.num_of_people < 2 or 8 < customer.num_of_people:
            return False
        count = 0
        for r in self.reserve_list:
            if customer.time == r.time:
                count += 1
            if 2 < count:
                return False
        self.reserve_list.append(customer)
        return True


def solution(customers, shops):
    hairshop = HairShop()
    restaurant = Restaurant()

    count = 0
    for customer, shop in zip(customers, shops):
        if shop == "hairshop":
            if hairshop.reserve(Customer(customer[0], customer[1], customer[2])):
                count += 1
        elif shop == "restaurant":
            if restaurant.reserve(Customer(customer[0], customer[1], customer[2])):
                count += 1
    return count


customers = [[1000, 2, 1], [2000, 2, 4], [
    1234, 5, 1], [4321, 2, 1], [1111, 3, 10]]
shops = ["hairshop", "restaurant", "hairshop", "hairshop", "restaurant"]
ret = solution(customers, shops)

print("solution 함수의 반환 값은", ret, "입니다.")
# 결과 : solution 함수의 반환 값은 3 입니다.
