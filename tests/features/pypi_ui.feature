Feature: PyPI critical user journeys
  As a user of pypi.org
  I want core discovery and account entry points to work
  So I can find and evaluate packages reliably

  Scenario: Home page loads core controls
    Given I open the PyPI home page
    Then the home page core controls are visible

  Scenario Outline: Search returns results for a known package
    Given I open the PyPI home page
    When I search for package "<package_name>"
    Then results are shown for package "<package_name>"

    Examples:
      | package_name |
      | requests     |

  Scenario Outline: Opening package details from search works
    Given I search and open package "<package_name>"
    Then package details are displayed for "<package_name>"
    And install command is visible for "<package_name>"

    Examples:
      | package_name |
      | requests     |

  Scenario Outline: Release history is accessible from package page
    Given I search and open package "<package_name>"
    When I open release history
    Then release history entries are visible

    Examples:
      | package_name |
      | requests     |

  Scenario: Login page shows required controls
    Given I open the login page
    Then login form controls are visible
