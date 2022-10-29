def main_func():
    print('This is main_func. Commit 1')
    print('This is main_func. Commit 2')
    print('This is main_func. Commit 3')


# <<<<<<< HEAD this is what was added in Commit 4, on branch main
def main_func2():
    print('This is main_func2. Commit 4')
# ======= end of what was added in Commit 4, on branch main

# this is what was added in Commit 2 on branch test
def test_func():
    print('This is test_func. Branch test. Commit 1)
    print('This is test_func. Branch test. Commit 2)
# >>>>>>> test --- end of what was added in Commit 2 on branch test
