# In order to include ui files, you need carry out to python code files.
# 	Sample command: pyuic4 SMS.ui -o SMS.py
# resources.qrc file too.
# 	Command: pyuic4 resources.qrc -o resources_rc.py
#
# And finally, it is necesary to generate a .ts file for each languaje
# you need.
# 	Sample command: pylupdate4 *ui -ts lang_fr.ts
#
# Once the .ts file is ready, it must be edited with Qt Linguist program.
# 	Sample command: linguist lang_fr
# 	
#
# Launch the app.
# 	Command: python main.py
#

UI_FILES	= SMS.ui\
						help_dialog.ui\
						sms_details.ui

RESOURCES = resources.qrc 

#SOURCES = SMS.py\
#					main.py\
#					__init__.py\
#					SMS_Help.py\
#					SMS_Send.py\
#					resources_rc.py

MAIN		= main.py

#python, pyuic4 and pyrcc4 binaries
PYTHON	= python
PYUIC		= pyuic4
PYRCC		= pyrcc4

clean :
	-rm *.pyc *~

all :
	make clean
	@echo "Launching main application ..."
	$(PYTHON) $(MAIN)
