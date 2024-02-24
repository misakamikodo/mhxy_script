# cmd /k  cd /d "$(CURRENT_DIRECTORY)" & python "$(FULL_CURRENT_PATH)" -i 1 & pause & exit
if __name__ == '__main__':
    sp = {"x":1,"y":2}
    print(sp.x)
