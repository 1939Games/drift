# -*- coding: utf-8 -*-

import os

from travispy import travispy
from travispy import TravisPy


def main():
    conn = TravisPy.github_auth(os.environ['GITHUB_KEY'], travispy.PRIVATE)
    repos = conn.repos()
    for repo in repos:
        build = conn.build(repo.last_build_id)
        if "kitrun.py" in build.config.get("script", [""])[0]:
            print "Found drift project: ", repo.slug
            if not build.running:
                print "Restarting..."
                build.restart()


if __name__ == "__main__":
    main()
