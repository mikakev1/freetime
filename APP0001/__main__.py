#!/usr/bin/python
import os
import sys
import math

import PyQt5.QtGui
import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtOpenGL

from PyQt5.Qsci import QsciScintilla, QsciLexerPython, QsciLexerCPP
from PyQt5.QtGui import QFont, QColor, QFont, QGuiApplication, QMatrix4x4, QOpenGLContext,QOpenGLShader, QOpenGLShaderProgram, QSurfaceFormat, QWindow 
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMenuBar, QTabWidget, QApplication
from PyQt5.QtOpenGL import QGL, QGLFormat, QGLWidget

class GLSLEditor(QsciScintilla):
  def __init__(self):
    super(GLSLEditor, self).__init__()
    lexer = QsciLexerCPP()
    lexer.setColor(QColor("blue"), 1) 
    self.setMarginLineNumbers(1, True)
    self.setMarginWidth(1, "-----")
    self.setMarginsBackgroundColor(QColor("green"))
    self.setCaretLineVisible(True)
    self.setCaretLineBackgroundColor(QColor("#ffe4e4"))
    self.setLexer(lexer)
    self.show()
    
class TabbedWindow(QMainWindow):
  def __init__(self, Parent=None):
    super(TabbedWindow, self).__init__(Parent)
    self.setGeometry(0, 0, 640, 480)
    self.setWindowTitle("Shader Editor")
    self.setupUI()
  
  def setupUI(self):
    menu_bar = QMenuBar()
    file = menu_bar.addMenu("&File")
    help = menu_bar.addMenu("&Help")
    build = menu_bar.addMenu("&Build")
    exit = menu_bar.addMenu("&Exit")    
    tabs = QTabWidget()
    centerwidget = QWidget()
    vshadertab = QWidget()
    fshadertab = QWidget()
    vshadertab_layout = QVBoxLayout(vshadertab)
    fshadertab_layout = QVBoxLayout(fshadertab)
    fshadereditor = GLSLEditor()
    vshadereditor = GLSLEditor()
    fshadertab_layout.addWidget(fshadereditor)
    vshadertab_layout.addWidget(vshadereditor)
    tabs.addTab(vshadertab, "Vertex Shader")
    tabs.addTab(fshadertab, "Fragment Shader")
    vbox = QVBoxLayout()
    vbox.addWidget(menu_bar)
    vbox.addWidget(tabs)
    centerwidget.setLayout(vbox)
    self.setCentralWidget(centerwidget)
    pass
 

    #def center(self):
      ##screen = QDesktopWidget().screenGeometry()
      ##size = self.geometry()
      ##self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
      #pass      

class GLWindow(QWindow):
    def __init__(self):
      super(GLWindow, self).__init__()
      self.title= "GLWindow"
      self.setGeometry(0, 0, 640, 480)
      self.setupUI()
      
    def setupUI(self):  
      self.setSurfaceType(QWindow.OpenGLSurface)
      self.renderctxt = QOpenGLContext(self)
      self.renderctxt.setFormat(self.requestedFormat())
      self.renderctxt.create()
      self.renderctxt.makeCurrent(self)
      self.glfunc = self.renderctxt.versionFunctions()
      self.glfunc.initializeOpenGLFunctions()
      
      
  

class GLWidget(QGLWidget):
    def __init__(self,Parent=None):
      super(GLWidget, self).__init__(Parent)
      self.autoBufferSwap=True
      
    def initializeGL(self):
      glClearColor(0.0, 0.0, 0.0, 0.0)
      glEnable(GL_DEPTH_TEST)
    
    def resizeGL(self, width, height):
      glViewport(0, 0, width, height)
      pass
    
    def paintGL(self):
      pass
    
    
    
      
  

if __name__=='__main__':
  app = QApplication(sys.argv)
  window = TabbedWindow()
  glwindow = GLWindow()
  glwindow.show()
  #window.setupUI()
  window.show()
  sys.exit(app.exec_())
  
    
