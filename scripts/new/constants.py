#!/usr/bin/python3

# Base folder
BASE_FOLDER = '/Users/marcosmr/Development/CEDAR/cedar-experiments-curation' # for IntelliJ execution
#BASE_FOLDER = '.' # for Jupyter execution

# Resources
#RESOURCES_FOLDER = BASE_FOLDER + '/' + 'resources'
#
# Workspace
WORKSPACE_FOLDER = BASE_FOLDER + '/' + 'workspace-new'
SAMPLES_FOLDER = 'samples'
SOURCE_SAMPLES_FOLDER = 'source'
FILTERED_SAMPLES_FOLDER = 'filtered'
#
# Data download
NCBI_DOWNLOAD_URL = 'https://ftp.ncbi.nih.gov/biosample/biosample_set.xml.gz'
NCBI_SAMPLES_FOLDER_DEST = WORKSPACE_FOLDER  + '/' + SAMPLES_FOLDER + '/' + SOURCE_SAMPLES_FOLDER
NCBI_SAMPLES_FILE_DEST = 'biosample_set.xml.gz'
#
# Filtering
NCBI_FILTER_INPUT_FILE = NCBI_SAMPLES_FOLDER_DEST + '/' + NCBI_SAMPLES_FILE_DEST
NCBI_FILTER_OUTPUT_FOLDER = WORKSPACE_FOLDER  + '/' + SAMPLES_FOLDER + '/' + FILTERED_SAMPLES_FOLDER
NCBI_FILTER_OUTPUT_FILE = NCBI_FILTER_OUTPUT_FOLDER + '/' + 'biosample_filtered.xml'
NCBI_FILTER_RELEVANT_ATTS = ['sex', 'tissue', 'disease', 'cell_type', 'cell type', 'cell_line', 'cell line', 'ethnicity']
NCBI_FILTER_MIN_RELEVANT_ATTS = 3
#
# Instances generation
# NCBI_INSTANCES_TRAINING_SET_SIZE = 222797 # 85% of 262,114
# NCBI_INSTANCES_TESTING_SET_SIZE = 39317 # 15% of 262,114
# NCBI_INSTANCES_MAX_FILES_PER_FOLDER = 10000
# NCBI_INSTANCES_INPUT_PATH = NCBI_FILTER_OUTPUT_FILE
# NCBI_INSTANCES_OUTPUT_BASE_PATH = WORKSPACE_FOLDER + '/cedar_instances/ncbi_cedar_instances'
# NCBI_INSTANCES_TRAINING_BASE_PATH = NCBI_INSTANCES_OUTPUT_BASE_PATH + '/training'
# NCBI_INSTANCES_TESTING_BASE_PATH = NCBI_INSTANCES_OUTPUT_BASE_PATH + '/testing'
# NCBI_INSTANCES_EXCLUDE_IDS = False
# NCBI_INSTANCES_EXCLUDED_IDS_FILE_PATH = RESOURCES_FOLDER + 'excluded_ids.txt'
# NCBI_INSTANCES_OUTPUT_BASE_FILE_NAME = 'ncbi_biosample_instance'
# NCBI_INSTANCES_EMPTY_BIOSAMPLE_INSTANCE_PATH = RESOURCES_FOLDER + '/cedar_artifacts/ncbi_biosample_empty_instance.json'




