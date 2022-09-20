"""CSC148 Assignment 1: Sample tests

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Assignment 2.

Warning: This is an extremely incomplete set of tests! Add your own tests
to be confident that your code is correct.

Note: this file is to only help you; you will not submit it when you hand in
the assignment.

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) University of Toronto
"""
# Note that some tests under each Task subheading depend on other methods
# implemented within that task, and previous tasks before it

from society import *


def sample_society0() -> Society:
    """Return a Society of sufficient complexity without District Leaders.
    """
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    c2 = Citizen(2, 'Citizen 2', 3002, 'Bank robber', 19)
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    c4 = Citizen(4, 'Citizen 4', 3004, 'Cook', 5)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.add_citizen(c4, 1)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c6 = Citizen(6, 'Citizen 6', 3006, 'Coach', 56)
    s.add_citizen(c5, 2)
    s.add_citizen(c6, 2)
    c8 = Citizen(8, 'Citizen 8', 3008, 'Farmer', 22)
    c9 = Citizen(9, 'Citizen 9', 3009, 'Farmer', 22)
    c10 = Citizen(10, 'Citizen 10', 3010, 'Driver', 22)
    s.add_citizen(c8, 6)
    s.add_citizen(c9, 6)
    s.add_citizen(c10, 6)
    c7 = Citizen(7, 'Citizen 7', 3007, 'Builder', 58)
    s.add_citizen(c7, 4)
    return s


def sample_society1() -> Society:
    """Return a Society of sufficient complexity with District leaders.
    """
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    c4 = Citizen(4, 'Citizen 4', 3004, 'Cook', 5)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.add_citizen(c4, 1)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c6 = Citizen(6, 'Citizen 6', 3006, 'Coach', 56)
    s.add_citizen(c5, 2)
    s.add_citizen(c6, 2)
    c8 = Citizen(8, 'Citizen 8', 3008, 'Farmer', 22)
    c9 = Citizen(9, 'Citizen 9', 3009, 'Farmer', 22)
    c10 = Citizen(10, 'Citizen 10', 3010, 'Driver', 22)
    s.add_citizen(c8, 6)
    s.add_citizen(c9, 6)
    s.add_citizen(c10, 6)
    c7 = DistrictLeader(7, 'Citizen 7', 3007, 'Builder', 58, 'D7')
    s.add_citizen(c7, 4)
    return s


def society_from_file_demo() -> Society:
    """Return the Society defined in the provided file citizens.csv.
    """
    return create_society_from_file(open("citizens.csv"))


def promote_citizen_example() -> Society:
    """Return the society used in the handout example of promotion.
    """
    c = DistrictLeader(6, "Star", 3036, "CFO", 20, "Area 52")
    c2 = DistrictLeader(5, "S.T.A.R.R.Y Lab", 3024, "Manager", 50, "Finance")
    c3 = Citizen(7, "Hookins", 3071, "Labourer", 60)
    c4 = Citizen(11, "Starky", 3036, "Repairer", 90)
    c5 = Citizen(13, "STARRY", 3098, "Eng", 86)
    s = Society()
    s.add_citizen(c)
    s.add_citizen(c2, 6)
    s.add_citizen(c3, 5)
    s.add_citizen(c4, 7)
    s.add_citizen(c5, 7)
    return s


###########################################################################
# Tests for methods in Task 1.1
###########################################################################


def test_add_subordinate() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c


def test_add_subordinate_in_order() -> None:
    """Test that Citizen.add_subordinate keeps the list of subordinates in
    ascending order by their ID """
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c2 = Citizen(2, 'Citizen 2', 3002, 'Janitor', 19)
    c.add_subordinate(c2)
    assert c.get_direct_subordinates() == [c2, c1]
    c3 = Citizen(30, 'Citizen 30', 3030, 'Comedian', 69)
    c.add_subordinate(c3)
    assert c.get_direct_subordinates() == [c2, c1, c3]
# ----------------------------------------------------------------------- #


def test_remove_subordinate() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c.remove_subordinate(11)
    assert c.get_direct_subordinates() == []
    assert c1.get_superior() is None


# ----------------------------------------------------------------------- #
def test_become_subordinate_to() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c1.become_subordinate_to(c)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c


def test_become_subordinate_to_none_when_already_none() -> None:
    """Test that Citizen.become_subordinate_to correctly handles the case when a
    citizen becomes subordinate to None when it already is a subordinate to None
    """
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c.become_subordinate_to(None)


# ----------------------------------------------------------------------- #
def test_get_citizen() -> None:
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    who = c5.get_citizen(5)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating] == \
           [5, 'Citizen 5', 3005, 'Farmer', 101]


###########################################################################
# Tests for methods in Task 1.2
###########################################################################

def test_get_all_subordinates() -> None:
    c1 = Citizen(10, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    result = c3.get_all_subordinates()
    assert result == [c2, c1]


# ----------------------------------------------------------------------- #
def test_get_society_head() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    head = c1.get_society_head()
    assert head is c3


# ----------------------------------------------------------------------- #
def test_get_closest_common_superior() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    c4.become_subordinate_to(c3)
    c5.become_subordinate_to(c4)
    assert c3.get_closest_common_superior(1) == c3


def test_get_closest_common_superior_self_is_direct_superior() -> None:
    """Test Citizen.get_closest_common_superior when self is a direct superior
    to the other citizen"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c1.become_subordinate_to(c2)
    assert c2.get_closest_common_superior(1) is c2


def test_get_closest_common_superior_other_is_direct_superior() -> None:
    """Test Citizen.get_closest_common_superior when the other citizen is a
    direct superior to self"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c2.become_subordinate_to(c1)
    assert c2.get_closest_common_superior(1) is c1


def test_get_closest_common_superior_self_is_indirect_superior() -> None:
    """Test Citizen.get_closest_common_superior when self is an indirect
    superior to the other citizen"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    assert c1.get_closest_common_superior(3) is c1


def test_get_closest_common_superior_other_is_indirect_superior() -> None:
    """Test Citizen.get_closest_common_superior when the other citizen is an
    indirect superior to self"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    assert c3.get_closest_common_superior(1) is c1


def test_get_closest_common_superior_direct() -> None:
    """Test Citizen.get_closest_common_superior when the closest common superior
    is a direct superior to both or only one of them"""
    c2 = Citizen(2, "Starky Industries", 3024, "Labourer", 50)
    c3 = Citizen(3, "Hookins National Lab", 3024, "Manager", 30)
    c4 = Citizen(4, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c2.become_subordinate_to(c3)
    c4.become_subordinate_to(c3)
    assert c2.get_closest_common_superior(4) is c3
    c1 = Citizen(1, "Starky Industries", 3025, "Comedian", 69)
    c1.become_subordinate_to(c2)
    assert c1.get_closest_common_superior(4) is c3
    c5 = Citizen(5, "Hookins National Lab", 3000, "Gamer", 99)
    c5.become_subordinate_to(c4)
    assert c2.get_closest_common_superior(5) is c3


def test_get_closest_common_superior_indirect() -> None:
    """Test Citizen.get_closest_common_superior when the closest common superior
    is an indirect superior to both them"""
    c1 = Citizen(1, "Starky Industries", 3025, "Comedian", 69)
    c2 = Citizen(2, "Starky Industries", 3024, "Labourer", 50)
    c3 = Citizen(3, "Hookins National Lab", 3024, "Manager", 30)
    c4 = Citizen(4, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c5 = Citizen(5, "Hookins National Lab", 3000, "Gamer", 99)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    c4.become_subordinate_to(c3)
    c5.become_subordinate_to(c4)
    assert c1.get_closest_common_superior(5) is c3


def test_get_closest_common_superior_self() -> None:
    """Test Citizen.get_closest_common_superior when called on the same
    citizen"""
    c1 = Citizen(1, "Starky Industries", 3025, "Comedian", 69)
    assert c1.get_closest_common_superior(1) is c1
###########################################################################
# Tests for methods in Task 1.3
###########################################################################


def test_society_get_citizen() -> None:
    s = sample_society0()
    who = s.get_citizen(5)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating] == \
           [5, 'Citizen 5', 3005, 'Farmer', 101]


# ----------------------------------------------------------------------- #
def test_get_all_citizens() -> None:
    s = sample_society0()
    result = [c.cid for c in s.get_all_citizens()]
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ----------------------------------------------------------------------- #
def test_add_citizen() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    s.add_citizen(c2)
    s.add_citizen(c1, 2)
    assert s.get_head() == c2
    assert s.get_citizen(1) is c1
    assert c1.get_superior() is c2


def test_add_citizen_new_head() -> None:
    """Test Society.add_citizen when the citizen being added has subordinates
    and becomes the new head"""
    c1 = Citizen(1, "Starky Industries", 3025, "Comedian", 69)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    c4 = Citizen(4, "Hookins National Lab", 3124, "Secretary", 40)
    c4.become_subordinate_to(c2)
    c3.become_subordinate_to(c2)
    s = Society(c2)
    s.add_citizen(c1)
    assert c1.get_superior() is None
    assert s.get_head() is c1
    assert c1.get_direct_subordinates() == [c2]
    assert c2.get_superior() is c1
    assert c2.get_direct_subordinates() == [c3, c4]


# ----------------------------------------------------------------------- #
def test_get_citizens_with_job() -> None:
    s = sample_society0()
    result = [c.cid for c in s.get_citizens_with_job('Farmer')]
    assert result == [5, 8, 9]


###########################################################################
# Tests for methods in Task 2.1
###########################################################################

def test_district_leader() -> None:
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 30, "District A")
    assert [d.cid, d.manufacturer, d.model_year, d.job, d.rating] == \
           [2, "Some Lab", 3024, "Lawyer", 30]
    assert d.get_district_name() == 'District A'


# ----------------------------------------------------------------------- #
def test_get_district_citizens() -> None:
    c1 = DistrictLeader(1, "Some Lab", 3024, "Commander", 65, "District A")
    c2 = Citizen(2, "Hookins National Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c1)
    assert c1.get_district_citizens() == [c1, c2, c3]


###########################################################################
# Tests for methods in Task 2.2
###########################################################################


def test_get_district_name() -> None:
    s = sample_society1()
    who = s.get_citizen(10)
    result = who.get_district_name()
    assert result == 'D2'


def test_get_district_name_has_district() -> None:
    """Test Citizen.get_district_name when this citizen is a DistrictLeader"""
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 30, "District A")
    assert d.get_district_name() == "District A"


def test_get_district_name_no_superior() -> None:
    """Test Citizen.get_district_name when this citizen is not a DistrictLeader
    and does not have a superior"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    assert c1.get_district_name() == ''


def test_get_district_name_superior_district() -> None:
    """Test Citizen.get_district_name when this citizen is not a DistrictLeader
    but has a superior that is a DistrictLeader"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 30, "District A")
    c1.become_subordinate_to(d)
    assert c1.get_district_name() == "District A"


def test_get_district_name_superior_no_district() -> None:
    """Test Citizen.get_district_name when this citizen is not a DistrictLeader,
    and has a superior that also is not a DistrictLeader"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c1.become_subordinate_to(c2)
    assert c1.get_district_name() == ''


# ----------------------------------------------------------------------- #
def test_rename_district() -> None:
    s = sample_society1()
    who = s.get_citizen(10)
    who.rename_district('D10')
    leader = s.get_citizen(2)
    assert leader.get_district_name() == 'D10'


def test_rename_district_has_district() -> None:
    """Test Citizen.rename_district when the citizen is a DistrictLeader"""
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 30, "District A")
    d.rename_district("Test")
    assert d.get_district_name() == "Test"


def test_rename_district_no_superior() -> None:
    """Test Citizen.rename_district when the citizen is not a DistrictLeader and
    has no superior"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    assert c1.rename_district("Test") is None


def test_rename_district_superior_district() -> None:
    """Test Citizen.rename_district when the citizen is not a DistrictLeader but
    has a superior that is a DistrictLeader"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 30, "District A")
    c1.become_subordinate_to(d)
    c1.rename_district("Test")
    assert d.get_district_name() == "Test"


def test_rename_district_superior_no_district() -> None:
    """Test Citizen.rename_district when this citizen is not a DistrictLeader,
    and has a superior that also is not a DistrictLeader"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c1.become_subordinate_to(c2)
    c1.rename_district("Test")
    assert c1.rename_district("Test") is None


###########################################################################
# Tests for method in Task 2.3
###########################################################################

def test_change_citizen_type() -> None:
    s = sample_society1()
    s.change_citizen_type(6, 'D6')
    who = s.get_citizen(6)
    assert isinstance(who, DistrictLeader)
    assert who.get_district_name() == 'D6'
    assert [c.cid for c in who.get_all_subordinates()] == [8, 9, 10]
    assert who.get_superior().cid == 2


def test_change_citizen_type_citizen_to_leader_isolated() -> None:
    """Test Society.change_citizen_type by changing a Citizen with no superior
    nor subordinates to a DistrictLeader"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    s = Society(c1)
    d = s.change_citizen_type(1, "Test")
    assert s._head is d
    assert c1 not in s.get_all_citizens()
    assert d.get_district_name() == "Test"
    assert d.get_all_subordinates() == []
    assert d.get_superior() is None


def test_change_citizen_type_citizen_to_leader_incorporated_head() -> None:
    """Test Society.change_citizen_type by changing a Citizen to a
    DistrictLeader. This Citizen has subordinates and is the head of the
    Society, thus he doesn't have a superior"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c3.become_subordinate_to(c2)
    s = Society(c2)
    d = s.change_citizen_type(2, "Test")
    assert s._head is d
    assert c2 not in s.get_all_citizens()
    assert d.get_district_name() == "Test"
    assert d.get_all_subordinates() == [c1, c3]
    assert (c1.get_superior() is d) and (c3.get_superior() is d)
    assert d.get_superior() is None


def test_change_citizen_type_citizen_to_leader_incorporated_bottom() -> None:
    """Test Society.change_citizen_type by changing a Citizen to a
    DistrictLeader. This Citizen doesn't have subordinates and is not the head
    of society"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c2.become_subordinate_to(c1)
    s = Society(c1)
    d = s.change_citizen_type(2, "Test")
    assert ((s._head is not d) or (s._head is not c2)) and (s._head is c1)
    assert c2 not in s.get_all_citizens() and \
           (d in c1.get_direct_subordinates())
    assert d.get_district_name() == "Test"
    assert d.get_all_subordinates() == []
    assert d.get_superior() is c1


def test_change_citizen_type_citizen_to_leader_incorporated_middle() -> None:
    """Test Society.change_citizen_type by changing a Citizen to a
    DistrictLeader. This Citizen has subordinates but is not the head of
    society"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c3.become_subordinate_to(c2)
    c2.become_subordinate_to(c1)
    s = Society(c1)
    d = s.change_citizen_type(2, "Test")
    assert ((s._head is not d) or (s._head is not c2)) and (s._head is c1)
    assert c2 not in s.get_all_citizens() and \
           (d in c1.get_direct_subordinates())
    assert d.get_district_name() == "Test"
    assert d.get_all_subordinates() == [c3]
    assert d.get_superior() is c1
    assert (c3.get_superior() is not c2) and (c3.get_superior() is d)


def test_change_citizen_type_leader_to_citizen_isolated() -> None:
    """Test Society.change_citizen_type by changing a DistrictLeader with no
    superior nor subordinates to a Citizen"""
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 30, "District A")
    s = Society(d)
    c1 = s.change_citizen_type(2)
    assert s._head is c1
    assert d not in s.get_all_citizens()
    assert isinstance(c1, Citizen)
    assert d.get_all_subordinates() == []
    assert d.get_superior() is None


def test_change_citizen_type_leader_to_citizen_incorporated_head() -> None:
    """Test Society.change_citizen_type by changing a DistrictLeader to a
    Citizen. This DistrictLeader has subordinates and is the head of the
    Society, thus he doesn't have a superior"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 30, "District A")
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(d)
    c3.become_subordinate_to(d)
    s = Society(d)
    c2 = s.change_citizen_type(2)
    assert s._head is c2
    assert d not in s.get_all_citizens()
    assert isinstance(c2, Citizen)
    assert c2.get_all_subordinates() == [c1, c3]
    assert (c1.get_superior() is c2) and (c3.get_superior() is c2)
    assert c2.get_superior() is None


def test_change_citizen_type_leader_to_citizen_incorporated_bottom() -> None:
    """Test Society.change_citizen_type by changing a DistrictLeader to a
    Citizen. This DistrictLeader doesn't have subordinates and is not the head
    of society"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 30, "District A")
    d.become_subordinate_to(c1)
    s = Society(c1)
    c2 = s.change_citizen_type(2)
    assert ((s._head is not d) or (s._head is not c2)) and (s._head is c1)
    assert (d not in s.get_all_citizens()) and (c2 in s.get_all_citizens())
    assert isinstance(c2, Citizen)
    assert c2.get_all_subordinates() == []
    assert c2.get_superior() is c1


def test_change_citizen_type_leader_to_citizen_incorporated_middle() -> None:
    """Test Society.change_citizen_type by changing a DistrictLeader to a
    Citizen. This DistrictLeader has subordinates but is not the head of
    society"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 30, "District A")
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c3.become_subordinate_to(d)
    d.become_subordinate_to(c1)
    s = Society(c1)
    c2 = s.change_citizen_type(2)
    assert ((s._head is not d) or (s._head is not c2)) and (s._head is c1)
    assert (d not in s.get_all_citizens()) and \
           (c2 in c1.get_direct_subordinates())
    assert isinstance(c2, Citizen)
    assert c2.get_all_subordinates() == [c3]
    assert c2.get_superior() is c1
    assert (c3.get_superior() is not d) and (c3.get_superior() is c2)


###########################################################################
# Tests for method in Task 3.1
###########################################################################

def test_swap_up_citizen_to_citizen_not_head() -> None:
    """Test Society._swap_up when the <citizen> does not have subordinates and
    his superior is not a DistrictLeader nor the head of society"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    s = Society(c1)
    s._swap_up(s.get_citizen(3))
    assert s.get_citizen(2).get_superior() is s.get_citizen(3)
    assert s.get_citizen(2).get_all_subordinates() == []
    assert s.get_citizen(3).get_superior() is s.get_citizen(1)
    assert s.get_citizen(3).get_direct_subordinates() == [s.get_citizen(2)]
    assert s.get_citizen(3) in s.get_citizen(1).get_direct_subordinates()
    assert isinstance(s.get_citizen(2), Citizen) and \
           isinstance(s.get_citizen(3), Citizen) and \
           isinstance(s.get_citizen(1), Citizen)
    assert s.get_citizen(2).job == "Commander" and \
           s.get_citizen(3).job == "Manager"


def test_swap_up_citizen_to_leader_head() -> None:
    """Test Society._swap_up when the <citizen> does not have subordinates and
    his superior is a DistrictLeader and the head of society"""
    d = DistrictLeader(1, "Some Lab", 3024, "Lawyer", 30, "District A")
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 40)
    c2.become_subordinate_to(d)
    s = Society(d)
    s._swap_up(s.get_citizen(2))
    assert s.get_citizen(2).get_superior() is None
    assert s.get_head() is s.get_citizen(2)
    assert s.get_citizen(2).get_direct_subordinates() == [s.get_citizen(1)]
    assert s.get_citizen(1).get_superior() is s.get_citizen(2)
    assert s.get_citizen(1).get_all_subordinates() == []
    assert isinstance(s.get_citizen(1), Citizen) and \
           isinstance(s.get_citizen(2), DistrictLeader)
    assert s.get_citizen(2).get_district_name() == "District A"
    assert s.get_citizen(2).job == "Lawyer" and \
           s.get_citizen(1).job == "Manager"


def test_swap_up_citizen_with_subs_to_leader_with_subs_not_head() -> None:
    """Test Society._swap_up when the <citizen> has subordinates and
    his superior is a DistrictLeader with other subordinates that is not the
    society head"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 30, "District A")
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Hookins National Lab", 3124, "Secretary", 40)
    c5 = Citizen(5, "S.T.A.R.R.Y Lab", 3089, "HR Employee", 60)
    c6 = Citizen(6, "Starky Industries", 3140, "Head of Technology", 70)
    d.become_subordinate_to(c1)
    c3.become_subordinate_to(d)
    c4.become_subordinate_to(d)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)
    s = Society(c1)
    s._swap_up(s.get_citizen(3))
    assert s.get_citizen(1).get_direct_subordinates() == [s.get_citizen(3)]
    assert s.get_citizen(3).get_superior() is s.get_citizen(1)
    assert s.get_citizen(3).get_direct_subordinates() == \
           [s.get_citizen(2), s.get_citizen(4)]
    assert s.get_citizen(2).get_superior() is s.get_citizen(3)
    assert s.get_citizen(2).get_direct_subordinates() == \
           [s.get_citizen(5), s.get_citizen(6)]
    assert isinstance(s.get_citizen(2), Citizen) and \
           isinstance(s.get_citizen(3), DistrictLeader)
    assert s.get_citizen(3).get_district_name() == "District A"
    assert s.get_citizen(2).job == "Commander" and \
           s.get_citizen(3).job == "Lawyer"


def test_promote_citizen() -> None:
    s = promote_citizen_example()
    s.promote_citizen(11)
    promoted = s.get_citizen(11)
    demoted = s.get_citizen(5)
    assert isinstance(promoted, DistrictLeader)
    assert promoted.get_district_name() == 'Finance'
    assert [c.cid for c in promoted.get_all_subordinates()] == [5, 7, 13]
    assert promoted.get_superior().cid == 6
    assert not isinstance(demoted, DistrictLeader)
    assert [c.cid for c in demoted.get_all_subordinates()] == [7, 13]
    assert demoted.get_superior() == promoted


def test_promote_citizen_lowest_rating() -> None:
    """Test Society.promote_citizen when the citizen being promoted has the
    lowest rating in the society"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 60)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 50)
    c2.become_subordinate_to(c1)
    s = Society(c1)
    s.promote_citizen(2)
    assert s.get_citizen(1).get_superior() is None
    assert s.get_head() is s.get_citizen(1)
    assert s.get_citizen(1).get_all_subordinates() == [s.get_citizen(2)]
    assert s.get_citizen(2).get_direct_subordinates() == []
    assert s.get_citizen(2).get_superior() is s.get_citizen(1)


def test_promote_citizen_equal_rating() -> None:
    """Test Society.promote_citizen when the citizen being promoted has the
    same rating as his superior"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 60)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 60)
    c2.become_subordinate_to(c1)
    s = Society(c1)
    s.promote_citizen(2)
    assert s.get_citizen(1).get_superior() is None
    assert s.get_head() is s.get_citizen(1)
    assert s.get_citizen(1).get_all_subordinates() == [s.get_citizen(2)]
    assert s.get_citizen(2).get_direct_subordinates() == []
    assert s.get_citizen(2).get_superior() is s.get_citizen(1)


def test_promote_citizen_leader() -> None:
    """Test Society.promote_citizen when the citizen being promoted is a
    DistrictLeader"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 70, "District A")
    d.become_subordinate_to(c1)
    s = Society(c1)
    s.promote_citizen(2)
    assert s.get_citizen(1).get_superior() is None
    assert s.get_head() is s.get_citizen(1)
    assert s.get_citizen(1).get_all_subordinates() == [s.get_citizen(2)]
    assert s.get_citizen(2).get_direct_subordinates() == []
    assert s.get_citizen(2).get_superior() is s.get_citizen(1)
    assert isinstance(s.get_citizen(2), DistrictLeader)


def test_promote_citizen_up_to_rating() -> None:
    """Test Society.promote_citizen until the citizen being promoted encounters
    another citizen with a higher rating"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 60)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 40)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 50)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    s = Society(c1)
    s.promote_citizen(3)
    assert s.get_citizen(1).get_superior() is None
    assert s.get_citizen(1).get_direct_subordinates() == [s.get_citizen(3)]
    assert s.get_head() is s.get_citizen(1)
    assert s.get_citizen(3).get_superior() is s.get_citizen(1)
    assert s.get_citizen(3).get_direct_subordinates() == [s.get_citizen(2)]
    assert s.get_citizen(2).get_superior() is s.get_citizen(3)
    assert s.get_citizen(2).get_direct_subordinates() == []
    assert s.get_citizen(1).job == "Labourer" and \
           s.get_citizen(3).job == "Manager" and \
           s.get_citizen(2).job == "Commander"


def test_promote_citizen_up_to_leader() -> None:
    """Test Society.promote_citizen until the citizen being promoted becomes a
    DistrictLeader. The """
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 40)
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 60, "District A")
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 50)
    c4 = Citizen(4, "Hookins National Lab", 3124, "Secretary", 70)
    c5 = Citizen(5, "S.T.A.R.R.Y Lab", 3089, "HR Employee", 100)
    d.become_subordinate_to(c1)
    c3.become_subordinate_to(d)
    c4.become_subordinate_to(c3)
    c5.become_subordinate_to(c4)
    s = Society(c1)
    s.promote_citizen(4)
    assert s.get_citizen(1).get_superior() is None
    assert s.get_citizen(1).get_direct_subordinates() == [s.get_citizen(4)]
    assert s.get_head() is s.get_citizen(1)
    assert s.get_citizen(4).get_superior() is s.get_citizen(1)
    assert s.get_citizen(4).get_direct_subordinates() == [s.get_citizen(2)]
    assert s.get_citizen(4).get_district_name() == "District A"
    assert s.get_citizen(2).get_superior() is s.get_citizen(4)
    assert s.get_citizen(2).get_direct_subordinates() == [s.get_citizen(3)]
    assert not isinstance(s.get_citizen(2), DistrictLeader)
    assert s.get_citizen(3).get_superior() is s.get_citizen(2)
    assert s.get_citizen(3).get_direct_subordinates() == [s.get_citizen(5)]
    assert not isinstance(s.get_citizen(3), DistrictLeader)
    assert s.get_citizen(5).get_superior() is s.get_citizen(3)
    assert s.get_citizen(5).get_all_subordinates() == []
    assert not isinstance(s.get_citizen(5), DistrictLeader)
    assert s.get_citizen(1).job == "Labourer" and \
           s.get_citizen(4).job == "Lawyer" and \
           s.get_citizen(2).job == "Commander" and \
           s.get_citizen(3).job == "Secretary" and \
           s.get_citizen(5).job == "HR Employee"


###########################################################################
# Tests for method in Task 3.2
###########################################################################

def test_get_highest_rated_subordinate() -> None:
    s = sample_society1()
    who = s.get_citizen(2)
    result = who.get_highest_rated_subordinate()
    assert result.cid == 5


# ----------------------------------------------------------------------- #
def test_delete_citizen() -> None:
    s = sample_society1()
    s.delete_citizen(6)
    who = s.get_citizen(2)
    assert [c.cid for c in who.get_direct_subordinates()] == [5, 8, 9, 10]
    assert s.get_citizen(6) is None


def test_delete_citizen_only_head() -> None:
    """Test Society.delete_citizen when the citizen being deleted is the only
    citizen in the society"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 40)
    s = Society(c1)
    s.delete_citizen(1)
    assert s.get_head() is None
    assert s.get_all_citizens() == []


def test_delete_citizen_no_subs() -> None:
    """Test Society.delete_citizen when the citizen being deleted has no
    subordinates and is not the head of society"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 40)
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 60, "District A")
    d.become_subordinate_to(c1)
    s = Society(c1)
    s.delete_citizen(2)
    assert d not in s.get_all_citizens()
    assert c1 in s.get_all_citizens()
    assert s.get_head() is c1
    assert d.get_superior() is None
    assert c1.get_all_subordinates() == []


def test_delete_citizen_subs_not_head() -> None:
    """Test Society.delete_citizen when the citizen being deleted has
    subordinates but is not the head of society"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 30, "District A")
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Hookins National Lab", 3124, "Secretary", 40)
    c5 = Citizen(5, "S.T.A.R.R.Y Lab", 3089, "HR Employee", 60)
    c6 = Citizen(6, "Starky Industries", 3140, "Head of Technology", 70)
    d.become_subordinate_to(c1)
    c3.become_subordinate_to(d)
    c4.become_subordinate_to(d)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)
    s = Society(c1)
    s.delete_citizen(2)
    assert s.get_head() is c1
    assert d not in s.get_all_citizens()
    assert c1.get_direct_subordinates() == [c3, c4]
    assert c3.get_superior() is c1
    assert c4.get_superior() is c1
    assert c3.get_direct_subordinates() == [c5, c6]
    assert c5.get_superior() is c3 and c6.get_superior() is c3


def test_delete_citizen_subs_head() -> None:
    """Test Society.delete_citizen when the citizen being deleted has
    subordinates and is the head of society"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 30, "District A")
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Hookins National Lab", 3124, "Secretary", 40)
    c5 = Citizen(5, "S.T.A.R.R.Y Lab", 3089, "HR Employee", 60)
    c6 = Citizen(6, "Starky Industries", 3140, "Head of Technology", 70)
    d.become_subordinate_to(c1)
    c3.become_subordinate_to(d)
    c4.become_subordinate_to(d)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)
    s = Society(c1)
    s.delete_citizen(1)
    assert s.get_head() is d
    assert c1 not in s.get_all_citizens()
    assert c1.get_all_subordinates() == []
    assert d.get_superior() is None
    s.delete_citizen(2)
    assert s.get_head() is c3
    assert d not in s.get_all_citizens()
    assert d.get_all_subordinates() == []
    assert c3.get_superior() is None
    assert c3.get_direct_subordinates() == [c4, c5, c6]
    assert c4.get_superior() is c3


if __name__ == '__main__':
    import pytest

    pytest.main(['a2_sample_test.py'])
