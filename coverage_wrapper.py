import pytest
from coverage import coverage

cov = coverage(omit='.tox*')
cov.start()

pytest.main()

cov.stop()
cov.save()
