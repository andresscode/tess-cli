class Directory:
    SOLUTIONS = 'solutions'
    CASES = 'cases'
    BUILD = 'build'
    TESS = '.tess'

    @staticmethod
    def all():
        return [Directory.SOLUTIONS, Directory.CASES, Directory.BUILD,
                Directory.TESS]
