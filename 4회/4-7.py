# 4회 - 문제 7. RPG스토리

"""
게임에 몬스터, 전사, 힐러 세 종류의 유닛이 있습니다. 
유닛들의 공격과 힐링에 따른 체력치의 변화를 계산하기 위해 아래와 같이 Unit, Monster, Warrior, Healer 클래스를 작성했습니다.

  ![unit_cpp.png](https://grepp-programmers.s3.amazonaws.com/files/ybm/24405fa391/86dc4e66-a77f-4a8d-917d-7579ec9b9700.png)

* Unit :
  * Unit : 유닛을 나타내는 클래스입니다.
  * HP : 유닛의 체력을 나타냅니다. 유닛의 초기 체력은 1,000입니다.
  * under_attack : 유닛이 공격을 받으면 유닛의 체력을 감소시킵니다.

* Monster :
  * Monster : 몬스터를 나타내는 클래스이며 Unit을 상속합니다.
  * attak_point : 몬스터의 공격력 입니다.
  * under_attack : 몬스터가 공격을 받으면 몬스터의 체력을 감소시킵니다.
  * attack : 몬스터의 attack_point를 return 합니다.

* Warrior :
  * Warrior : 전사를 나타내는 클래스이며 Unit을 상속합니다.
  * attak_point : 전사의 공격력 입니다.
  * under_attack : 전사가 공격을 받으면 전사의 체력을 감소시킵니다.
  * attack : 전사의 attack_point를 return 합니다.

* Healer : 
  * Healer : 힐러를 나타내는 클래스이며 Unit을 상속합니다.
  * healing_point : 힐러의 회복치 입니다.
  * under_attack : 힐러가 공격을 받으면 힐러의 체력을 감소시킵니다.
  * healing : 대상 유닛의 체력을 healing_point 만큼 회복시킵니다.  회복 후 대상 유닛의 체력은 기본 체력 1,000보다 커질 수 있습니다.

게임에서 각 유닛들이 다음과 같이 행동 했을 때, 몬스터, 전사, 힐러의 남은 체력을 구하려 합니다.

* 몬스터가 전사와 힐러를 한 번씩 공격했습니다.
* 전사가 몬스터를 한 번 공격했습니다.
* 힐러가 몬스터와 전사의 체력을 한 번씩 회복했습니다.

몬스터의 공력력 monster_attack_point, 전사의 공격력 warrior_attack_point, 힐러의 회복치 healing_point가 매개변수로 주어질 때, 각 유닛이 행동을 마친 후 몬스터, 전사, 힐러의 남은 체력을 순서대로 리스트에 담아 return 하도록 solution 함수를 작성하려 합니다. 위 클래스 구조를 참고하여 주어진 코드의 빈칸을 적절히 채워 전체 코드를 완성해주세요.


---
#####매개변수 설명
몬스터의 공력력 monster_attack_point, 전사의 공격력 warrior_attack_point, 힐러의 회복치 healing_point가 solution 함수의 매개변수로 주어집니다.

* monster_attack_point는 1 이상 500 이하의 자연수입니다.
* warrior_attack_point는 1 이상 500 이하의 자연수입니다.
* healing_point는 1 이상 500 이하의 자연수입니다.

---
#####return 값 설명
각 유닛이 문제에 주어진 행동을 마친 후 몬스터, 전사, 힐러의 남은 체력을 순서대로 리스트에 담아 return 해주세요.

---
#####예시

| monster_attack_point | warrior_attack_point | healing_point | return          |
|----------------------|----------------------|---------------|-----------------|
| 100                  | 90                   | 30            | [940, 930, 900] |

#####예시 설명

* 몬스터 공격력 : 100
* 전사 공격력 : 90
* 힐러 회복치 : 30

몬스터가 전사와 힐러를 한 번씩 공격하면 각 유닛의 남은 체력은 다음과 같습니다.

| 몬스터 체력 | 전사 체력 | 힐러 체력 |
|-------------|-----------|-----------|
| 1000        | 900       | 900       |

전사가 몬스터를 한 번 공격하면 각 유닛의 남은 체력은 다음과 같습니다.

| 몬스터 체력 | 전사 체력 | 힐러 체력 |
|-------------|-----------|-----------|
| 910        | 900       | 900       |

힐러가 몬스터와 전사의 체력을 한 번씩 회복하면 각 유닛의 남은 체력은 다음과 같습니다.

| 몬스터 체력 | 전사 체력 | 힐러 체력 |
|-------------|-----------|-----------|
| 940        | 930       | 900       |

따라서 [940, 930, 900]을 return 하면 됩니다.
"""

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


class Unit:
    def __init__(self):
        self.HP = 1000

    def under_attack(self, damage):
        pass


class Monster(Unit):
    def __init__(self, attack_point):
        super().__init__()
        self.attack_point = attack_point

    def under_attack(self, damage):
        self.HP -= damage

    def attack(self):
        return self.attack_point


class Warrior(Unit):
    def __init__(self, attack_point):
        super().__init__()
        self.attack_point = attack_point

    def under_attack(self, damage):
        self.HP -= damage

    def attack(self):
        return self.attack_point


class Healer(Unit):
    def __init__(self, healing_point):
        super().__init__()
        self.healing_point = healing_point

    def under_attack(self, damage):
        self.HP -= damage

    def healing(self, unit):
        unit.HP += self.healing_point


def solution(monster_attack_point, warrior_attack_point, healing_point):
    monster = Monster(monster_attack_point)
    warrior = Warrior(warrior_attack_point)
    healer = Healer(healing_point)

    monster.under_attack(warrior.attack())
    warrior.under_attack(monster.attack())
    healer.under_attack(monster.attack())
    healer.healing(warrior)
    healer.healing(monster)

    answer = [monster.HP, warrior.HP, healer.HP]
    return answer


monster_attack_point = 100
warrior_attack_point = 90
healing_point = 30
ret = solution(monster_attack_point, warrior_attack_point, healing_point)

print("solution 함수의 반환 값은", ret, "입니다.")
# 결과 : solution 함수의 반환 값은 [940, 930, 900] 입니다.
