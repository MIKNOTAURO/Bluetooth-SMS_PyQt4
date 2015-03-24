# In order to include ui files, you need carry out to python code files.
# 	Sample command: pyuic4 sms.ui -o SMS.py
# resources.qrc file too.
# 	Command: pyuic4 resources.qrc -o resources_rc.py
#
# And finally, it is necesary to generate a .ts file for each languaje
# you need.
# 	Sample command: pylupdate4 *ui -ts lang_fr.ts
#
# Once the .ts file is ready, it must be edited with Qt Linguist program.
# 	Sample command: linguist lang_fr.ts
# 	After translate all, it's necessary to Release the translation file:
# 	Go to File menu > Release. A new lang_fr.qm file will be created (don't delete it)
# 	
#
# Launch the app.
#	$ python main.py
#

UI_FILES	= 	sms.ui			\
			  	help_dialog.ui	\
				sms_details.ui

RESOURCES 	= 	resources.qrc 

#SOURCES 	= 	SMS.py			\
#				main.py			\
#				__init__.py		\
#				SMS_Help.py		\
#				SMS_Send.py		\
#				resources_rc.py

MAIN		= 	main.py

# python, pyuic4 and pyrcc4 binaries
PYTHON		= 	python
PYUIC		= 	pyuic4
PYRCC		= 	pyrcc4
RM			=	rm -v
GARBAGE		= 	*.pyc *~

compile:
	# translations
	lrelease lang_es.ts -compress -qm lang_es.qm
	lrelease lang_en.ts -compress -qm lang_en.qm
	# ui
	pyuic4 sms.ui -o SMS.py
	pyuic4 sms_details.ui -o SMS_Send.py
	pyuic4 help_dialog.ui -o SMS_Help.py
	# resources
	pyrcc4 resources.qrc -o resources_rc.py
	echo "Compilation done!"

run:
	make compile
	make first

all:
	make run

first: clean
	$(PYTHON) $(MAIN)

clean :
	- $(RM) $(GARBAGE)

