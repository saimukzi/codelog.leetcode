#!/bin/bash

set -e

javac JTest.java
java  JTest

javac QuickSelect.java && java QuickSelect
