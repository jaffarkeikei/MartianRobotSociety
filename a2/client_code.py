"""Assignment 2: Client Code

CSC148, Winter 2022

This code is provided solely for the personal and private use of students
taking the CSC148 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of this
code, whether as given or with any changes, are expressly prohibited.

Authors: Sadia Sharmin, Diane Horton, Dina Sabie, Sophia Huynh, and
         Jonathan Calver.

All of the files in this directory and all subdirectories are:
Copyright (c) 2022 Sadia Sharmin, Diane Horton, Dina Sabie, Sophia Huynh, and
                   Jonathan Calver

=== Module description ===
This module contains client code that calls upon the classes specified in
society_hierarchy.py.

You should NOT modify this code.

This code is used by society_ui.py to demonstrate sample usage of how the
functionality of the code you are completing in society_hierarchy.py might be
used in an application.

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.
"""

from typing import Optional, Tuple, List
from society_hierarchy import Citizen, Society, DistrictLeader, \
    create_society_from_file


class SocietySimulator:
    """SocietySimulator: a class that stores information about the current
    state of a simulated Society.

    === Public Attributes ===
    current_citizen:
        The Citizen currently being displayed in the simulation.
    current_subordinates:
        The list of subordinates currently being displayed in the simulation.
    displaying_direct:
        Whether the current_subordinates being displayed are only the direct
        subordinates of current_citizen or not.
    current_society:
        The Society currently being displayed in the simulation.
    """
    current_citizen: Optional[Citizen]
    current_subordinates: List[Citizen]
    displaying_direct: bool
    current_society: Society

    def __init__(self) -> None:
        """Initialize this SocietySimulator with an empty Society.
        """
        self.current_society = Society()
        self.current_citizen = None
        self.current_subordinates = []
        self.displaying_direct = True

    # === Uses code from Task 1 ===

    def display_citizen(self, cid: int) -> None:
        """Update the current Citizen to be the Citizen with the ID <cid>.
        If no such Citizen exist, the current Citizen should be None.
        """
        self.current_citizen = self.current_society.get_citizen(cid)

    def get_current_citizen_details(self) -> Tuple[int, str, int, int,
                                                   str, str]:
        """Return the current Citizen's id, manufacturer, salary, job, and
        district. If the current Citizen is None, then
        (0, "", 0, 0, "", "") is returned.
        """
        if self.current_citizen:
            return (self.current_citizen.cid,
                    self.current_citizen.manufacturer,
                    self.current_citizen.model_year,
                    self.current_citizen.rating,
                    self.current_citizen.job,
                    self.get_current_citizen_district())

        return 0, "", 0, 0, "", ""

    def get_current_superior(self) -> Optional[Citizen]:
        """Return the superior of the current Citizen.

        If no superior exists, return None.
        """
        if self.current_citizen:
            return self.current_citizen.get_superior()

        return None

    def create_citizen(self, cid: int, manufacturer: str, model_year: int,
                       rating: int, job: str,
                       superior_id: int) -> None:
        """Create the Citizen with the manufacturer <manufacturer>,
        ID <cid>, job <job>, rating <rating>, and set their superior
        to be the Citizen with ID <superior_id>.

        If <superior_id> == 0, this Citizen is the new head of the
        Society.

        If <cid> is already in use or < 1, raise an error.

        Pre-condition: <superior_id> == 0 or is an ID that appears in the
        Society.
        """
        # Check if cid is valid
        if cid < 1 or self.current_society.get_citizen(cid) is not None:
            raise ValueError

        # Create the Citizen
        new_citizen = Citizen(cid, manufacturer, model_year, job, rating)

        # Add the Citizen to the Society
        if superior_id == 0:
            self.current_society.add_citizen(new_citizen)
        else:
            self.current_society.add_citizen(new_citizen, superior_id)

        self.display_citizen(cid)

    def find_citizens_with_job(self, job: str) -> List[Citizen]:
        """Return a list of all citizens in the current Society with the
        job named <job> in order of increasing cids.
        """
        return self.current_society.get_citizens_with_job(job)

    def display_direct_subordinates(self) -> None:
        """Update the list of subordinates to display the current Citizen's
        direct subordinates.

        Subordinates must be in order of increasing cids.
        """
        self.displaying_direct = True

        if self.current_citizen:
            self.current_subordinates = \
                self.current_citizen.get_direct_subordinates()

    def display_all_subordinates(self) -> None:
        """Update the list of subordinates to display all of the current
        Citizen's subordinates.

        Subordinates must be in order of increasing cids.
        """
        self.displaying_direct = False

        if self.current_citizen:
            self.current_subordinates = \
                self.current_citizen.get_all_subordinates()

    def get_society_head(self) -> Citizen:
        """Return the head of the Society.

        The head of the Society is defined as the Citizen that does not
        have any superiors.

        Pre-condition: self.current_citizen is not None
        """
        return self.current_citizen.get_society_head()

    def get_common_superior(self, cid: int) -> Citizen:
        """Return the closest common _superior in the Society between
        the current Citizen and the Citizen with ID cid.

        Pre-conditions: self.current_citizen is not None
                        there is a Citizen with ID cid in the society

        """
        return self.current_citizen.get_closest_common_superior(cid)

    # === Uses code from Task 2 ===
    def is_district_leader(self) -> bool:
        """Return True if the current Citizen is a DistrictLeader.
        """

        return isinstance(self.current_citizen, DistrictLeader)

    def get_current_citizen_district(self) -> str:
        """Return the immediate district that self.current_citizen belongs to.

        If the current Citizen is not part of any districts, return "".
        """

        if self.current_citizen:
            return self.current_citizen.get_district_name()

        return ''

    def find_district_citizens(self) -> List[Citizen]:
        """Return a list of citizens in the current Citizen's district
        (including the current Citizen) and all subdistricts in
        order of increasing cids.

        Pre-condition: self.current_citizen is a DistrictLeader.
        """

        if isinstance(self.current_citizen, DistrictLeader):
            return self.current_citizen.get_district_citizens()
        return []

    def rename_current_district(self, district_name: str) -> None:
        """Change the current Citizen's immediate district leader's district to
        be <district_name>.
        """

        self.current_citizen.rename_district(district_name)

    def become_district_leader(self, district_name: str) -> None:
        """Make the current Citizen the DistrictLeader of a new district with
        the name <district_name>.

        Pre-condition: self.current_citizen is not already a DistrictLeader.
        """

        self.current_citizen = self.current_society. \
            change_citizen_type(self.current_citizen.cid, district_name)

    def become_citizen(self) -> None:
        """Make the current Citizen a regular Citizen instead of a
        DistrictLeader.

        Pre-condition: self.current_citizen is a DistrictLeader.
        """
        # Keep the Citizen's ID number so we can update self.current_citizen
        # to the Citizen version afterwards.
        cid = self.current_citizen.cid

        self.current_society.change_citizen_type(cid)

        # Update the current Citizen being displayed
        self.current_citizen = self.current_society.get_citizen(cid)

    # === Uses code from Task 3 ===
    def delete_citizen(self, cid: int) -> None:
        """Delete the Citizen with ID cid from the current Society.

        If this Citizen has subordinates, their subordinates become
        subordinates of the Citizen's superior.

        If the head of the Society is deleted, their most highly rated
        subordinate becomes the new head.

        Pre-condition: there is a Citizen with the cid <cid> in
        self.current_society.
        """
        previous_id = self.current_citizen.cid

        self.current_society.delete_citizen(cid)

        if previous_id == cid:
            self.current_citizen = self.current_society.get_head()

    def promote_citizen(self, cid: int) -> None:
        """Promote the Citizen with the cid <cid> in the current Society
        until they have a superior with a higher rating than them or until they
        become the leader of their district.

        Precondition: There is a Citizen in self.current_society with
        cid <cid>.
        """
        self.current_society.promote_citizen(cid)

        self.current_citizen = \
            self.current_society.get_citizen(self.current_citizen.cid)

    def file_to_society(self, filename: str) -> None:
        """Read the Society data in the file named <filename>, creating a
        Society from it and setting it as the current Society.
        Set the current Citizen to the head of the Society.
        """
        with open(filename) as f:
            self.current_society = create_society_from_file(f)
            self.current_citizen = self.current_society.get_head()

    def get_all_district_names(self) -> List[str]:
        """Return a list containing all the district names in
        the current society"""
        society_head = self.current_society.get_head()
        if not society_head:
            return []
        district_names = []
        if society_head.get_district_name():
            district_names.append(district_names)
        for subordinate in society_head.get_all_subordinates():
            if isinstance(subordinate, DistrictLeader):
                district_names.append(subordinate.get_district_name())
        return district_names


if __name__ == "__main__":
    pass
