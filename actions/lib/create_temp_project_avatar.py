from base import JiraBaseAction


class JiraCreateTempProjectAvatar(JiraBaseAction):
    def _run(self, project, filename, size, **kwargs):
      avatar_img = open(filename, "r")
      return self.jira.create_temp_project_avatar(project, filename, size, avatar_img.read(), **kwargs)

