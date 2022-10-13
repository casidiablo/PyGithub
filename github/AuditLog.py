############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

import github.GithubObject
import github.NamedUser
import github.Organization
import github.Repository


class AuditLog(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents Events. The reference can be found here https://docs.github.com/en/rest/orgs/orgs#get-the-audit-log-for-an-organization
    """

    def __repr__(self):
        return self.get__repr__({"actor": self._actor.value, "action": self._action.value})

    @property
    def actor(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        return self._actor.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        return self._created_at.value

    @property
    def org(self):
        """
        :type: :class:`github.Organization.Organization`
        """
        return self._org.value

    @property
    def user(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        return self._user.value

    @property
    def actor_location(self):
        """
        :type: string
        """
        return self._actor_location.value
    
    @property
    def repo(self):
        """
        :type: :class:`github.Repository.Repository`
        """
        return self._repo.value

    @property
    def action(self):
        """
        :type: string
        """
        return self._action.value

    @property
    def pull_request_id(self):
        """
        :type: string
        """
        return self._pull_request_id.value

    @property
    def operation_type(self):
        """
        :type: string
        """
        return self._operation_type.value

    @property
    def pull_request_title(self):
        """
        :type: string
        """
        return self._pull_request_title.value

    @property
    def pull_request_url(self):
        """
        :type: string
        """
        return self._pull_request_url.value

    def _initAttributes(self):
        self._actor = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._org = github.GithubObject.NotSet
        self._repo = github.GithubObject.NotSet
        self._action = github.GithubObject.NotSet
        self._actor_location = github.GithubObject.NotSet
        self._pull_request_id = github.GithubObject.NotSet
        self._operation_type = github.GithubObject.NotSet
        self._pull_request_title = github.GithubObject.NotSet
        self._pull_request_url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "action" in attributes:  # pragma no branch
            self._action = self._makeStringAttribute(attributes["action"])
        if "operation_type" in attributes:  # pragma no branch
            self._operation_type = self._makeStringAttribute(attributes["operation_type"])
        if "actor" in attributes:  # pragma no branch
            self._actor = self._makeStringAttribute(attributes["actor"])
        if "actor_location" in attributes:  # pragma no branch
            self._actor_location = self._makeStringAttribute(attributes["actor_location"]["country_code"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeIntAttribute(attributes["created_at"])
        if "org" in attributes:  # pragma no branch
            self._org = self._makeStringAttribute(attributes["org"])

        if "repo" in attributes:  # pragma no branch
            self._repo = self._makeStringAttribute(attributes["repo"].lstrip(f"{self._org.value}/"))
        elif "public_repo" in attributes:  # pragma no branch
            self._repo = self._makeStringAttribute(attributes["public_repo"].lstrip(f"{self._org.value}/"))

        if "pull_request_url" in attributes:  # pragma no branch
            self._pull_request_url = self._makeStringAttribute(attributes["pull_request_url"])
        if "pull_request_id" in attributes:  # pragma no branch
            self._pull_request_id = self._makeIntAttribute(
                attributes["pull_request_id"]
            )
        if "pull_request_title" in attributes:  # pragma no branch
            self._pull_request_title = self._makeStringAttribute(attributes["pull_request_title"])