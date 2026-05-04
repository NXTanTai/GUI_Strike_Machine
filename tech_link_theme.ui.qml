<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1024</width>
    <height>720</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
    <horstretch>0</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="maximumSize">
   <size>
    <width>16777215</width>
    <height>16777215</height>
   </size>
  </property>
  <property name="font">
   <font>
    <pointsize>8</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>Tech-Link - Production System</string>
  </property>
  <property name="windowIcon">
   <iconset resource="../../../../../Pictures/QT_Icon/Icon.qrc">
    <normaloff>:/newPrefix/Logo_Cty_2.png</normaloff>:/newPrefix/Logo_Cty_2.png</iconset>
  </property>
  <property name="styleSheet">
   <string notr="true">QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #F8FAFC, stop:1 #E2E8F0);
            }
            QTabWidget::pane {
                border: 1px solid #E5E5E5;
                background-color: white;
                border-radius: 8px;
            }
            QTabWidget::tab-bar {
                alignment: left;
            }
            QTabBar::tab {
                background-color: #F1F5F9;
                border: 1px solid #E5E5E5;
                padding: 12px 24px;
                margin-right: 2px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                color: #64748B;
                font-weight: 500;
            }
            QTabBar::tab:selected {
                background-color: white;
                border-bottom-color: white;
                color: #0B7EC8;
            }
            QTabBar::tab:hover:!selected {
                background-color: #E2E8F0;
            }</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="minimumSize">
    <size>
     <width>1024</width>
     <height>720</height>
    </size>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <property name="spacing">
     <number>5</number>
    </property>
    <property name="leftMargin">
     <number>5</number>
    </property>
    <property name="topMargin">
     <number>5</number>
    </property>
    <property name="rightMargin">
     <number>5</number>
    </property>
    <property name="bottomMargin">
     <number>5</number>
    </property>
    <item>
     <widget class="QFrame" name="header_frame">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>0</width>
        <height>50</height>
       </size>
      </property>
      <property name="styleSheet">
       <string notr="true">QFrame {
    background-color: white;
    border-radius: 12px;
    border: none;
}</string>
      </property>
      <property name="frameShape">
       <enum>QFrame::NoFrame</enum>
      </property>
      <layout class="QHBoxLayout" name="horizontalLayout">
       <property name="leftMargin">
        <number>10</number>
       </property>
       <property name="topMargin">
        <number>5</number>
       </property>
       <property name="rightMargin">
        <number>5</number>
       </property>
       <property name="bottomMargin">
        <number>5</number>
       </property>
       <item>
        <widget class="QFrame" name="logo_frame">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="minimumSize">
          <size>
           <width>40</width>
           <height>35</height>
          </size>
         </property>
         <property name="maximumSize">
          <size>
           <width>16777215</width>
           <height>16777215</height>
          </size>
         </property>
         <property name="styleSheet">
          <string notr="true">QFrame {
    background-color: transparent;
    border-radius: 8px;
    image: url(:/newPrefix/Logo_Cty_2.png);
}</string>
         </property>
         <property name="frameShape">
          <enum>QFrame::NoFrame</enum>
         </property>
        </widget>
       </item>
       <item>
        <layout class="QVBoxLayout" name="company_header_layout">
         <item>
          <widget class="QLabel" name="company_name">
           <property name="sizePolicy">
            <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
             <horstretch>0</horstretch>
             <verstretch>0</verstretch>
            </sizepolicy>
           </property>
           <property name="styleSheet">
            <string notr="true">    font-size: 24px;
    font-weight: bold;
    color: #1E293B;
    letter-spacing: 1px;</string>
           </property>
           <property name="text">
            <string>TECH-LINK</string>
           </property>
          </widget>
         </item>
        </layout>
       </item>
       <item>
        <layout class="QVBoxLayout" name="pc_inform_label">
         <item>
          <spacer name="horizontalSpacer_4">
           <property name="orientation">
            <enum>Qt::Horizontal</enum>
           </property>
           <property name="sizeHint" stdset="0">
            <size>
             <width>0</width>
             <height>0</height>
            </size>
           </property>
          </spacer>
         </item>
        </layout>
       </item>
       <item>
        <widget class="QPushButton" name="pushButton">
         <property name="text">
          <string>PushButton</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="pushButton_2">
         <property name="text">
          <string>PushButton</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QDateTimeEdit" name="dateTimeEdit">
         <property name="styleSheet">
          <string notr="true">font-size: 14px; 
color: rgb(0, 0, 0);
font-weight: 500;
padding: 5px;
border: none;
</string>
         </property>
         <property name="readOnly">
          <bool>true</bool>
         </property>
         <property name="buttonSymbols">
          <enum>QAbstractSpinBox::NoButtons</enum>
         </property>
         <property name="dateTime">
          <datetime>
           <hour>0</hour>
           <minute>0</minute>
           <second>0</second>
           <year>2026</year>
           <month>1</month>
           <day>1</day>
          </datetime>
         </property>
         <property name="maximumTime">
          <time>
           <hour>23</hour>
           <minute>59</minute>
           <second>59</second>
          </time>
         </property>
         <property name="displayFormat">
          <string>dd/MM/yyyy h:mm AP</string>
         </property>
         <property name="timeSpec">
          <enum>Qt::LocalTime</enum>
         </property>
        </widget>
       </item>
       <item>
        <layout class="QVBoxLayout" name="sys_state_layout">
         <item alignment="Qt::AlignHCenter">
          <widget class="QLabel" name="online_label">
           <property name="sizePolicy">
            <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
             <horstretch>0</horstretch>
             <verstretch>0</verstretch>
            </sizepolicy>
           </property>
           <property name="styleSheet">
            <string notr="true">font-size: 14px; 
border: 2px solid #E5E5E5; 
color: #10B981; 
font-weight: 500; 
padding-right: 3px;</string>
           </property>
           <property name="text">
            <string>🟢 Running</string>
           </property>
          </widget>
         </item>
        </layout>
       </item>
      </layout>
     </widget>
    </item>
    <item>
     <widget class="QTabWidget" name="tabWidget">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="font">
       <font>
        <family>Script MT Bold</family>
        <pointsize>15</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="styleSheet">
       <string notr="true">
QTabWidget::pane {
	border: 1px solid #E5E5E5;
	background-color: white;
	border-radius: 8px;
}
QTabWidget::tab-bar {
    alignment: left;
}
QTabWidget::tab-bar {
    alignment: left;
}
QTabBar::tab {
    background-color: #F1F5F9;
    border: 1px solid #E5E5E5;
    padding: 8px 16px;
    margin-right: 2px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    color: #64748B;
    font-weight: 500;
}
QTabBar::tab:selected {
    background-color: white;
    border-bottom-color: white;
    color: #0B7EC8;
}
QTabBar::tab:hover:!selected {
    background-color: #E2E8F0;
}</string>
      </property>
      <property name="currentIndex">
       <number>0</number>
      </property>
      <property name="iconSize">
       <size>
        <width>35</width>
        <height>35</height>
       </size>
      </property>
      <property name="elideMode">
       <enum>Qt::ElideNone</enum>
      </property>
      <widget class="QWidget" name="production_tab">
       <attribute name="icon">
        <iconset resource="../../../../../Pictures/QT_Icon/Icon.qrc">
         <normaloff>:/newPrefix/robotic_arm_robot_technology_tech_icon_233261.png</normaloff>:/newPrefix/robotic_arm_robot_technology_tech_icon_233261.png</iconset>
       </attribute>
       <attribute name="title">
        <string>Pressure Tab</string>
       </attribute>
       <layout class="QVBoxLayout" name="verticalLayout_2">
        <property name="leftMargin">
         <number>0</number>
        </property>
        <property name="topMargin">
         <number>0</number>
        </property>
        <property name="rightMargin">
         <number>0</number>
        </property>
        <property name="bottomMargin">
         <number>0</number>
        </property>
        <item>
         <widget class="QFrame" name="line_main_layout_3">
          <property name="sizePolicy">
           <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="styleSheet">
           <string notr="true"/>
          </property>
          <property name="frameShape">
           <enum>QFrame::StyledPanel</enum>
          </property>
          <property name="frameShadow">
           <enum>QFrame::Raised</enum>
          </property>
          <layout class="QVBoxLayout" name="verticalLayout_28" stretch="1,15,2">
           <property name="leftMargin">
            <number>0</number>
           </property>
           <property name="topMargin">
            <number>0</number>
           </property>
           <property name="rightMargin">
            <number>0</number>
           </property>
           <property name="bottomMargin">
            <number>0</number>
           </property>
           <item>
            <widget class="QWidget" name="widget_61" native="true">
             <layout class="QHBoxLayout" name="horizontalLayout_10">
              <property name="leftMargin">
               <number>5</number>
              </property>
              <property name="topMargin">
               <number>5</number>
              </property>
              <property name="rightMargin">
               <number>5</number>
              </property>
              <property name="bottomMargin">
               <number>5</number>
              </property>
              <item>
               <widget class="QLabel" name="label_123">
                <property name="font">
                 <font>
                  <pointsize>79</pointsize>
                 </font>
                </property>
                <property name="text">
                 <string>Test Group A</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QComboBox" name="material_selection_combobox">
                <property name="sizePolicy">
                 <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                  <horstretch>0</horstretch>
                  <verstretch>0</verstretch>
                 </sizepolicy>
                </property>
                <property name="minimumSize">
                 <size>
                  <width>226</width>
                  <height>40</height>
                 </size>
                </property>
                <property name="styleSheet">
                 <string notr="true">QComboBox {
    border: 1px solid #D1D5DB;
    border-radius: 6px;
    padding: 10px 12px;
    font-size: 14px;
    background-color: white;
    min-width: 200px;
}
QComboBox:hover {
    border: 1px solid #0B7EC8;
}
QComboBox:focus {
    border: 2px solid #0B7EC8;
}
QComboBox::drop-down {
    border: none;
    width: 30px;
}
QComboBox::down-arrow {
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 6px solid #64748B;
    margin-right: 8px;
}
QComboBox QAbstractItemView {
    border: 1px solid #E5E5E5;
    border-radius: 6px;
    background-color: white;
    selection-background-color: #0B7EC8;
    selection-color: black;
    padding: 4px;
}</string>
                </property>
                <property name="currentText">
                 <string>Product Data</string>
                </property>
                <property name="iconSize">
                 <size>
                  <width>35</width>
                  <height>35</height>
                 </size>
                </property>
                <item>
                 <property name="text">
                  <string>Product Data</string>
                 </property>
                </item>
               </widget>
              </item>
             </layout>
            </widget>
           </item>
           <item>
            <widget class="QScrollArea" name="scrollArea">
             <property name="sizePolicy">
              <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
               <horstretch>0</horstretch>
               <verstretch>0</verstretch>
              </sizepolicy>
             </property>
             <property name="styleSheet">
              <string notr="true">QFrame {
    background-color: #F8FAFC;
    border-left: 4px solid rgb(0, 231, 0);
    border-radius: 6px;
}
QStackedWidget {
	border: none;
}</string>
             </property>
             <property name="verticalScrollBarPolicy">
              <enum>Qt::ScrollBarAlwaysOn</enum>
             </property>
             <property name="sizeAdjustPolicy">
              <enum>QAbstractScrollArea::AdjustIgnored</enum>
             </property>
             <property name="widgetResizable">
              <bool>true</bool>
             </property>
             <widget class="QWidget" name="scrollAreaWidgetContents">
              <property name="geometry">
               <rect>
                <x>0</x>
                <y>0</y>
                <width>989</width>
                <height>843</height>
               </rect>
              </property>
              <property name="styleSheet">
               <string notr="true">
    background-color: #F8FAFC;
	padding: 2px;
</string>
              </property>
              <layout class="QVBoxLayout" name="verticalLayout_49">
               <property name="leftMargin">
                <number>0</number>
               </property>
               <property name="topMargin">
                <number>0</number>
               </property>
               <property name="rightMargin">
                <number>5</number>
               </property>
               <property name="bottomMargin">
                <number>0</number>
               </property>
               <item>
                <widget class="QWidget" name="widget_15" native="true">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="styleSheet">
                  <string notr="true"/>
                 </property>
                 <layout class="QHBoxLayout" name="horizontalLayout_11" stretch="1,0,2,0">
                  <property name="leftMargin">
                   <number>0</number>
                  </property>
                  <property name="topMargin">
                   <number>0</number>
                  </property>
                  <property name="rightMargin">
                   <number>0</number>
                  </property>
                  <property name="bottomMargin">
                   <number>0</number>
                  </property>
                  <item>
                   <widget class="QWidget" name="widget_71" native="true">
                    <property name="sizePolicy">
                     <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                      <horstretch>0</horstretch>
                      <verstretch>0</verstretch>
                     </sizepolicy>
                    </property>
                    <layout class="QVBoxLayout" name="verticalLayout_48" stretch="21">
                     <property name="leftMargin">
                      <number>0</number>
                     </property>
                     <property name="topMargin">
                      <number>0</number>
                     </property>
                     <property name="rightMargin">
                      <number>0</number>
                     </property>
                     <property name="bottomMargin">
                      <number>5</number>
                     </property>
                     <item>
                      <widget class="QWidget" name="widget_30" native="true">
                       <property name="styleSheet">
                        <string notr="true">border-left: None;
border-radius: 5px;</string>
                       </property>
                       <layout class="QVBoxLayout" name="verticalLayout_34" stretch="1,21">
                        <property name="leftMargin">
                         <number>5</number>
                        </property>
                        <property name="topMargin">
                         <number>0</number>
                        </property>
                        <property name="rightMargin">
                         <number>0</number>
                        </property>
                        <property name="bottomMargin">
                         <number>0</number>
                        </property>
                        <item>
                         <widget class="QWidget" name="widget_72" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_29">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_21" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_49" stretch="4,0">
                              <property name="spacing">
                               <number>7</number>
                              </property>
                              <property name="leftMargin">
                               <number>5</number>
                              </property>
                              <property name="topMargin">
                               <number>5</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>5</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_57">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <pointsize>12</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>Name</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_69">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <pointsize>12</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>PV Value A</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_2" native="true">
                          <layout class="QVBoxLayout" name="verticalLayout_14">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_28" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_19" stretch="0,0,0">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_58">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>Air Into Setting:</string>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QDoubleSpinBox" name="pv_value_A_1">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true">border: none;</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="suffix">
                                 <string/>
                                </property>
                                <property name="decimals">
                                 <number>0</number>
                                </property>
                                <property name="maximum">
                                 <double>999.000000000000000</double>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_79">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>%</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                           <item>
                            <widget class="QWidget" name="widget_29" native="true">
                             <property name="styleSheet">
                              <string notr="true"/>
                             </property>
                             <layout class="QHBoxLayout" name="horizontalLayout_18" stretch="0,0,0">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_59">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>Temp Setting:</string>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QDoubleSpinBox" name="pv_value_A_2">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true">border: none;</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="decimals">
                                 <number>1</number>
                                </property>
                                <property name="maximum">
                                 <double>999.000000000000000</double>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_84">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>°C</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                           <item>
                            <widget class="QWidget" name="widget_31" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_20" stretch="0,0,0">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_60">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>Filling time:</string>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QDoubleSpinBox" name="pv_value_A_3">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true">border: none;</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_89">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>s</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                           <item>
                            <widget class="QWidget" name="widget_33" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_21" stretch="0,0,0">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_61">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>Intake size setting:</string>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QSpinBox" name="pv_value_A_4">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true">border: none;</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="maximum">
                                 <number>999</number>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_80">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>%</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                           <item>
                            <widget class="QWidget" name="widget_32" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_22" stretch="0,0,0">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_62">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>In-test Pressure/Flow:</string>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QSpinBox" name="pv_value_A_5">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true">border: none;</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="maximum">
                                 <number>999</number>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_82">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>%</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                           <item>
                            <widget class="QWidget" name="widget_34" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_23" stretch="0,0,0">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_63">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>Inlet Temperature:</string>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QDoubleSpinBox" name="pv_value_A_6">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true">border: none;</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="decimals">
                                 <number>1</number>
                                </property>
                                <property name="maximum">
                                 <double>999.000000000000000</double>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_85">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>°C</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                           <item>
                            <widget class="QWidget" name="widget_41" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_30" stretch="0,0,0">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_70">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>Vacuum Pumpe:</string>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QDoubleSpinBox" name="pv_value_A_7">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true">border: none;</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="maximum">
                                 <double>999.000000000000000</double>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_91">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>s</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                           <item>
                            <widget class="QWidget" name="widget_39" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_28" stretch="0,0,0">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_68">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>Outlet size setting:</string>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QDoubleSpinBox" name="pv_value_A_8">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true">border: none;</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_81">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>%</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                           <item>
                            <widget class="QWidget" name="widget_35" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_24" stretch="0,0,0">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_64">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>Gas holding time:</string>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QDoubleSpinBox" name="pv_value_A_9">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true">border: none;</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_94">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>s</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                           <item>
                            <widget class="QWidget" name="widget_36" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_25" stretch="0,0,0">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_65">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>Medium Temperature:</string>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QDoubleSpinBox" name="pv_value_A_10">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true">border: none;</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_86">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>°C</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                           <item>
                            <widget class="QWidget" name="widget_38" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_27" stretch="0,0,0">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_67">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>Bleeding time:</string>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QSpinBox" name="pv_value_A_11">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true">border: none;</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="maximum">
                                 <number>999</number>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_90">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>s</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                           <item>
                            <widget class="QWidget" name="widget_37" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_26" stretch="0,0,0">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_66">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>Terminal Temperature:</string>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QDoubleSpinBox" name="pv_value_A_13">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true">border: none;</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="maximum">
                                 <double>999.000000000000000</double>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_87">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>°C</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                           <item>
                            <widget class="QWidget" name="widget_42" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_31" stretch="0,0,0">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_71">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>Vacuum Size Setting:</string>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QSpinBox" name="pv_value_A_14">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true">border: none;</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="maximum">
                                 <number>999</number>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_83">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>%</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                           <item>
                            <widget class="QWidget" name="widget_43" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_32" stretch="0,0,0">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_72">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>Oil Filling:</string>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QDoubleSpinBox" name="pv_value_A_15">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true">border: none;</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="decimals">
                                 <number>1</number>
                                </property>
                                <property name="maximum">
                                 <double>999.000000000000000</double>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_93">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>s</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                           <item>
                            <widget class="QWidget" name="widget_44" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_33" stretch="0,0,0">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_73">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>Interval of oil filling:</string>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QSpinBox" name="pv_value_A_16">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true">border: none;</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_92">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>s</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                           <item>
                            <widget class="QWidget" name="widget_45" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_34" stretch="0,0,0">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>5</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QLabel" name="label_74">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>Vacuum Pressure:</string>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QDoubleSpinBox" name="pv_value_A_17">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true">border: none;</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_88">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>°C</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                       </layout>
                      </widget>
                     </item>
                    </layout>
                   </widget>
                  </item>
                  <item>
                   <widget class="Line" name="line_4">
                    <property name="orientation">
                     <enum>Qt::Vertical</enum>
                    </property>
                   </widget>
                  </item>
                  <item>
                   <widget class="QWidget" name="widget_16" native="true">
                    <property name="styleSheet">
                     <string notr="true">border-left: None;</string>
                    </property>
                    <layout class="QVBoxLayout" name="verticalLayout_15" stretch="1,21">
                     <property name="leftMargin">
                      <number>0</number>
                     </property>
                     <property name="topMargin">
                      <number>0</number>
                     </property>
                     <property name="rightMargin">
                      <number>0</number>
                     </property>
                     <property name="bottomMargin">
                      <number>5</number>
                     </property>
                     <item>
                      <widget class="QWidget" name="widget_62" native="true">
                       <layout class="QHBoxLayout" name="horizontalLayout_12">
                        <property name="leftMargin">
                         <number>0</number>
                        </property>
                        <property name="topMargin">
                         <number>0</number>
                        </property>
                        <property name="rightMargin">
                         <number>0</number>
                        </property>
                        <property name="bottomMargin">
                         <number>0</number>
                        </property>
                        <item>
                         <widget class="QWidget" name="widget_20" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_356" stretch="4,1">
                           <property name="leftMargin">
                            <number>5</number>
                           </property>
                           <property name="topMargin">
                            <number>5</number>
                           </property>
                           <property name="rightMargin">
                            <number>5</number>
                           </property>
                           <property name="bottomMargin">
                            <number>5</number>
                           </property>
                           <item>
                            <widget class="QLabel" name="label_52">
                             <property name="sizePolicy">
                              <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                               <horstretch>0</horstretch>
                               <verstretch>0</verstretch>
                              </sizepolicy>
                             </property>
                             <property name="font">
                              <font>
                               <pointsize>12</pointsize>
                               <weight>75</weight>
                               <italic>false</italic>
                               <bold>true</bold>
                              </font>
                             </property>
                             <property name="text">
                              <string>SV Value A</string>
                             </property>
                             <property name="alignment">
                              <set>Qt::AlignCenter</set>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QLabel" name="label_268">
                             <property name="text">
                              <string/>
                             </property>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                       </layout>
                      </widget>
                     </item>
                     <item>
                      <widget class="QWidget" name="widget_24" native="true">
                       <property name="styleSheet">
                        <string notr="true">QDoubleSpinBox
{
    border: 1px solid #D1D5DB;
    border-radius: 6px;
}
QSpinBox
{
    border: 1px solid #D1D5DB;
    border-radius: 6px;
}</string>
                       </property>
                       <layout class="QVBoxLayout" name="verticalLayout_24">
                        <property name="leftMargin">
                         <number>0</number>
                        </property>
                        <property name="topMargin">
                         <number>0</number>
                        </property>
                        <property name="rightMargin">
                         <number>0</number>
                        </property>
                        <property name="bottomMargin">
                         <number>0</number>
                        </property>
                        <item>
                         <widget class="QWidget" name="widget_115" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_104" stretch="1">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_117" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_106" stretch="4,1">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>0</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QDoubleSpinBox" name="sv_value_A_1">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true"/>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="suffix">
                                 <string/>
                                </property>
                                <property name="decimals">
                                 <number>0</number>
                                </property>
                                <property name="maximum">
                                 <double>999.000000000000000</double>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_131">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>%</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_118" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_107" stretch="1">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_120" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_109" stretch="4,1">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>0</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QDoubleSpinBox" name="sv_value_A_2">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="decimals">
                                 <number>1</number>
                                </property>
                                <property name="maximum">
                                 <double>999.000000000000000</double>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_133">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>°C</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_121" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_110" stretch="1">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_123" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_112" stretch="4,1">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>0</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QDoubleSpinBox" name="sv_value_A_3">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_135">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>s</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_124" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_113" stretch="1">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_126" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_115" stretch="4,1">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>0</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QSpinBox" name="sv_value_A_4">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="maximum">
                                 <number>999</number>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_137">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>%</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_127" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_116" stretch="1">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_129" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_118" stretch="4,1">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>0</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QSpinBox" name="sv_value_A_5">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="maximum">
                                 <number>999</number>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_130">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>%</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_130" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_119" stretch="1">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_132" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_121" stretch="4,1">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>0</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QDoubleSpinBox" name="sv_value_A_6">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="decimals">
                                 <number>1</number>
                                </property>
                                <property name="maximum">
                                 <double>999.000000000000000</double>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_139">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>°C</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_133" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_122" stretch="1">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_135" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_124" stretch="4,1">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>0</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QDoubleSpinBox" name="sv_value_A_7">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="maximum">
                                 <double>999.000000000000000</double>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_141">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>s</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_136" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_125" stretch="1">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_138" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_127" stretch="4,1">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>0</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QDoubleSpinBox" name="sv_value_A_8">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_143">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>°C</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_139" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_128" stretch="1">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_141" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_130" stretch="4,1">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>0</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QDoubleSpinBox" name="sv_value_A_9">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="styleSheet">
                                 <string notr="true"/>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_145">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>°C</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_142" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_131" stretch="1">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_144" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_133" stretch="4,1">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>0</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QDoubleSpinBox" name="sv_value_A_10">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_147">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>s</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_145" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_134" stretch="1">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_147" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_136" stretch="4,1">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>0</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QSpinBox" name="sv_value_A_11">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="maximum">
                                 <number>999</number>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_149">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>%</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_151" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_140" stretch="1">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_153" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_142" stretch="4,1">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>0</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QDoubleSpinBox" name="sv_value_A_13">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="maximum">
                                 <double>999.000000000000000</double>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_153">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>s</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_154" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_143" stretch="1">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_156" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_145" stretch="4,1">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>0</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QSpinBox" name="sv_value_A_14">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="maximum">
                                 <number>999</number>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_155">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>%</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_157" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_146" stretch="1">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_159" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_148" stretch="4,1">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>0</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QDoubleSpinBox" name="sv_value_A_15">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                                <property name="decimals">
                                 <number>1</number>
                                </property>
                                <property name="maximum">
                                 <double>999.000000000000000</double>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_157">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>s</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_160" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_149" stretch="1">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_162" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_151" stretch="4,1">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>0</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QSpinBox" name="sv_value_A_16">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_159">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>s</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_163" native="true">
                          <layout class="QHBoxLayout" name="horizontalLayout_152" stretch="1">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QWidget" name="widget_165" native="true">
                             <layout class="QHBoxLayout" name="horizontalLayout_154" stretch="4,1">
                              <property name="leftMargin">
                               <number>0</number>
                              </property>
                              <property name="topMargin">
                               <number>0</number>
                              </property>
                              <property name="rightMargin">
                               <number>0</number>
                              </property>
                              <property name="bottomMargin">
                               <number>0</number>
                              </property>
                              <item>
                               <widget class="QDoubleSpinBox" name="sv_value_A_17">
                                <property name="sizePolicy">
                                 <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                                  <horstretch>0</horstretch>
                                  <verstretch>0</verstretch>
                                 </sizepolicy>
                                </property>
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignCenter</set>
                                </property>
                                <property name="readOnly">
                                 <bool>true</bool>
                                </property>
                                <property name="buttonSymbols">
                                 <enum>QAbstractSpinBox::NoButtons</enum>
                                </property>
                               </widget>
                              </item>
                              <item>
                               <widget class="QLabel" name="label_161">
                                <property name="font">
                                 <font>
                                  <family>Segoe UI</family>
                                  <pointsize>15</pointsize>
                                  <weight>75</weight>
                                  <italic>false</italic>
                                  <bold>true</bold>
                                 </font>
                                </property>
                                <property name="text">
                                 <string>°C</string>
                                </property>
                                <property name="alignment">
                                 <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
                                </property>
                               </widget>
                              </item>
                             </layout>
                            </widget>
                           </item>
                          </layout>
                         </widget>
                        </item>
                       </layout>
                      </widget>
                     </item>
                    </layout>
                   </widget>
                  </item>
                  <item>
                   <widget class="Line" name="line_3">
                    <property name="orientation">
                     <enum>Qt::Vertical</enum>
                    </property>
                   </widget>
                  </item>
                 </layout>
                </widget>
               </item>
              </layout>
             </widget>
            </widget>
           </item>
           <item>
            <widget class="QWidget" name="widget_4" native="true">
             <layout class="QHBoxLayout" name="horizontalLayout_4">
              <item>
               <layout class="QHBoxLayout" name="operation_btn_layout" stretch="1,1">
                <property name="spacing">
                 <number>10</number>
                </property>
                <item>
                 <widget class="QStackedWidget" name="start_stop_btn_layout">
                  <property name="maximumSize">
                   <size>
                    <width>16777215</width>
                    <height>150</height>
                   </size>
                  </property>
                  <property name="currentIndex">
                   <number>0</number>
                  </property>
                  <widget class="QWidget" name="start_btn_layout">
                   <layout class="QHBoxLayout" name="horizontalLayout_37">
                    <property name="leftMargin">
                     <number>0</number>
                    </property>
                    <property name="topMargin">
                     <number>0</number>
                    </property>
                    <property name="rightMargin">
                     <number>0</number>
                    </property>
                    <property name="bottomMargin">
                     <number>0</number>
                    </property>
                    <item>
                     <widget class="QPushButton" name="start_btn">
                      <property name="sizePolicy">
                       <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                        <horstretch>0</horstretch>
                        <verstretch>0</verstretch>
                       </sizepolicy>
                      </property>
                      <property name="maximumSize">
                       <size>
                        <width>16777215</width>
                        <height>150</height>
                       </size>
                      </property>
                      <property name="styleSheet">
                       <string notr="true">QPushButton {
    background-color: #10B981;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 500;
}
QPushButton:hover {
    background-color: #059669;
}
QPushButton:pressed {
	color: white;
    background-color: #085A91;
}</string>
                      </property>
                      <property name="text">
                       <string>▶️ Start</string>
                      </property>
                      <property name="checkable">
                       <bool>false</bool>
                      </property>
                     </widget>
                    </item>
                   </layout>
                  </widget>
                  <widget class="QWidget" name="stop_btn_layout">
                   <layout class="QHBoxLayout" name="horizontalLayout_38">
                    <property name="leftMargin">
                     <number>0</number>
                    </property>
                    <property name="topMargin">
                     <number>0</number>
                    </property>
                    <property name="rightMargin">
                     <number>0</number>
                    </property>
                    <property name="bottomMargin">
                     <number>0</number>
                    </property>
                    <item>
                     <widget class="QPushButton" name="stop_btn">
                      <property name="sizePolicy">
                       <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                        <horstretch>0</horstretch>
                        <verstretch>0</verstretch>
                       </sizepolicy>
                      </property>
                      <property name="maximumSize">
                       <size>
                        <width>16777215</width>
                        <height>150</height>
                       </size>
                      </property>
                      <property name="styleSheet">
                       <string notr="true">QPushButton {
    background-color: #EF4444;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 500;
}
QPushButton:hover {
    background-color: rgb(222, 0, 0)
}
QPushButton:pressed {
	color: white;
    background-color: #085A91;
}</string>
                      </property>
                      <property name="text">
                       <string>⏹️ Stop</string>
                      </property>
                      <property name="checkable">
                       <bool>false</bool>
                      </property>
                     </widget>
                    </item>
                   </layout>
                  </widget>
                 </widget>
                </item>
                <item>
                 <widget class="QPushButton" name="pause_btn">
                  <property name="sizePolicy">
                   <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                    <horstretch>0</horstretch>
                    <verstretch>0</verstretch>
                   </sizepolicy>
                  </property>
                  <property name="maximumSize">
                   <size>
                    <width>16777215</width>
                    <height>150</height>
                   </size>
                  </property>
                  <property name="styleSheet">
                   <string notr="true">QPushButton {
    background-color: white;
    color: #0B7EC8;
    border: 1px solid #0B7EC8;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 500;
}
QPushButton:hover {
    background-color: #F0F9FF;
}
QPushButton:pressed {
	color: white;
    background-color: #085A91;
}
QPushButton:checked {
	color: #0B7EC8;
    background-color: rgb(255, 255, 0);
}</string>
                  </property>
                  <property name="text">
                   <string>⏸️ Pause</string>
                  </property>
                  <property name="checkable">
                   <bool>true</bool>
                  </property>
                 </widget>
                </item>
               </layout>
              </item>
              <item>
               <widget class="QPushButton" name="pause_btn_2">
                <property name="sizePolicy">
                 <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                  <horstretch>0</horstretch>
                  <verstretch>0</verstretch>
                 </sizepolicy>
                </property>
                <property name="maximumSize">
                 <size>
                  <width>16777215</width>
                  <height>150</height>
                 </size>
                </property>
                <property name="styleSheet">
                 <string notr="true">QPushButton {
    background-color: white;
    color: #0B7EC8;
    border: 1px solid #0B7EC8;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 500;
}
QPushButton:hover {
    background-color: #F0F9FF;
}
QPushButton:pressed {
	color: white;
    background-color: #085A91;
}
QPushButton:checked {
	color: #0B7EC8;
    background-color: rgb(255, 255, 0);
}</string>
                </property>
                <property name="text">
                 <string>⏸️ Pause</string>
                </property>
                <property name="checkable">
                 <bool>true</bool>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QPushButton" name="pause_btn_3">
                <property name="sizePolicy">
                 <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                  <horstretch>0</horstretch>
                  <verstretch>0</verstretch>
                 </sizepolicy>
                </property>
                <property name="maximumSize">
                 <size>
                  <width>16777215</width>
                  <height>150</height>
                 </size>
                </property>
                <property name="styleSheet">
                 <string notr="true">QPushButton {
    background-color: white;
    color: #0B7EC8;
    border: 1px solid #0B7EC8;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 500;
}
QPushButton:hover {
    background-color: #F0F9FF;
}
QPushButton:pressed {
	color: white;
    background-color: #085A91;
}
QPushButton:checked {
	color: #0B7EC8;
    background-color: rgb(255, 255, 0);
}</string>
                </property>
                <property name="text">
                 <string>⏸️ Pause</string>
                </property>
                <property name="checkable">
                 <bool>true</bool>
                </property>
               </widget>
              </item>
             </layout>
            </widget>
           </item>
          </layout>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="products_tab">
       <attribute name="icon">
        <iconset>
         <normaloff>../../../../Borunte_2110A_Gui_Alter</normaloff>../../../../Borunte_2110A_Gui_Alter</iconset>
       </attribute>
       <attribute name="title">
        <string>🧪 Temperature</string>
       </attribute>
       <layout class="QHBoxLayout" name="horizontalLayout_9" stretch="0">
        <property name="spacing">
         <number>7</number>
        </property>
        <property name="leftMargin">
         <number>0</number>
        </property>
        <property name="topMargin">
         <number>0</number>
        </property>
        <property name="rightMargin">
         <number>0</number>
        </property>
        <property name="bottomMargin">
         <number>0</number>
        </property>
        <item>
         <widget class="QStackedWidget" name="detail_stacked_widget">
          <property name="currentIndex">
           <number>0</number>
          </property>
          <widget class="QWidget" name="detail_page_1">
           <layout class="QVBoxLayout" name="verticalLayout_10">
            <property name="leftMargin">
             <number>0</number>
            </property>
            <property name="topMargin">
             <number>0</number>
            </property>
            <property name="rightMargin">
             <number>0</number>
            </property>
            <property name="bottomMargin">
             <number>0</number>
            </property>
            <item>
             <widget class="QFrame" name="line_main_layout_2">
              <property name="sizePolicy">
               <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                <horstretch>0</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="styleSheet">
               <string notr="true">QFrame {
    background-color: #F8FAFC;
    border-left: 4px solid rgb(255, 0, 0);
    border-radius: 6px;
}
QStackedWidget {
	border: none;
}</string>
              </property>
              <property name="frameShape">
               <enum>QFrame::StyledPanel</enum>
              </property>
              <property name="frameShadow">
               <enum>QFrame::Raised</enum>
              </property>
              <layout class="QVBoxLayout" name="verticalLayout_27">
               <property name="leftMargin">
                <number>5</number>
               </property>
               <property name="topMargin">
                <number>5</number>
               </property>
               <property name="rightMargin">
                <number>5</number>
               </property>
               <property name="bottomMargin">
                <number>5</number>
               </property>
               <item>
                <widget class="QWidget" name="widget" native="true">
                 <layout class="QHBoxLayout" name="horizontalLayout_3">
                  <property name="leftMargin">
                   <number>0</number>
                  </property>
                  <property name="topMargin">
                   <number>0</number>
                  </property>
                  <property name="rightMargin">
                   <number>0</number>
                  </property>
                  <property name="bottomMargin">
                   <number>0</number>
                  </property>
                  <item>
                   <widget class="QWidget" name="widget_5" native="true">
                    <property name="styleSheet">
                     <string notr="true">border-left: None;
border-radius: 6px;
font: bold;</string>
                    </property>
                    <layout class="QVBoxLayout" name="verticalLayout_18">
                     <property name="leftMargin">
                      <number>5</number>
                     </property>
                     <property name="topMargin">
                      <number>5</number>
                     </property>
                     <property name="rightMargin">
                      <number>5</number>
                     </property>
                     <property name="bottomMargin">
                      <number>5</number>
                     </property>
                     <item>
                      <widget class="QLabel" name="label_5">
                       <property name="text">
                        <string>Name</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label">
                       <property name="text">
                        <string>Air Into Setting</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_3">
                       <property name="text">
                        <string>Temp Setting</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_4">
                       <property name="text">
                        <string>Filling time</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_6">
                       <property name="text">
                        <string>Intake size setting</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_7">
                       <property name="text">
                        <string>In-test pressure/Flow</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_8">
                       <property name="text">
                        <string>Inlet Temperature</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_9">
                       <property name="text">
                        <string>Gas holding time</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_10">
                       <property name="text">
                        <string>Medium Temperature</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_11">
                       <property name="text">
                        <string>Terminal Temperature</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_12">
                       <property name="text">
                        <string>Bleeding time</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_13">
                       <property name="text">
                        <string>Outlet size setting</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_14">
                       <property name="text">
                        <string>Vacuum Pressure</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_15">
                       <property name="text">
                        <string>Vacuum Pumpe</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_16">
                       <property name="text">
                        <string>Vacuum Size Setting</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_17">
                       <property name="text">
                        <string>Oil Filling</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_18">
                       <property name="text">
                        <string>Interval of oil filling</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_19">
                       <property name="text">
                        <string>Vacuum Pressure</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_20">
                       <property name="text">
                        <string>Start Count</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_21">
                       <property name="text">
                        <string>Equipment Operation</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_22">
                       <property name="text">
                        <string>Oil Pump ON/OFF</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="label_23">
                       <property name="text">
                        <string>Vacuum Pressure ON/OFF</string>
                       </property>
                      </widget>
                     </item>
                    </layout>
                   </widget>
                  </item>
                  <item>
                   <widget class="QWidget" name="widget_12" native="true">
                    <property name="sizePolicy">
                     <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                      <horstretch>0</horstretch>
                      <verstretch>0</verstretch>
                     </sizepolicy>
                    </property>
                    <layout class="QHBoxLayout" name="horizontalLayout_8">
                     <property name="leftMargin">
                      <number>0</number>
                     </property>
                     <property name="topMargin">
                      <number>0</number>
                     </property>
                     <property name="rightMargin">
                      <number>0</number>
                     </property>
                     <property name="bottomMargin">
                      <number>0</number>
                     </property>
                     <item>
                      <widget class="Line" name="line">
                       <property name="orientation">
                        <enum>Qt::Vertical</enum>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QWidget" name="widget_3" native="true">
                       <property name="styleSheet">
                        <string notr="true">border-left: None;
</string>
                       </property>
                       <layout class="QHBoxLayout" name="horizontalLayout_6">
                        <property name="leftMargin">
                         <number>0</number>
                        </property>
                        <property name="topMargin">
                         <number>5</number>
                        </property>
                        <property name="rightMargin">
                         <number>0</number>
                        </property>
                        <property name="bottomMargin">
                         <number>5</number>
                        </property>
                        <item>
                         <widget class="QWidget" name="widget_8" native="true">
                          <layout class="QVBoxLayout" name="verticalLayout_22" stretch="0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QLabel" name="label_26">
                             <property name="text">
                              <string>PV Value</string>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_27">
                             <property name="decimals">
                              <number>0</number>
                             </property>
                             <property name="maximum">
                              <double>999.000000000000000</double>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_28">
                             <property name="decimals">
                              <number>1</number>
                             </property>
                             <property name="maximum">
                              <double>999.000000000000000</double>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_4"/>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_19">
                             <property name="maximum">
                              <number>999</number>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_20">
                             <property name="maximum">
                              <number>999</number>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_29">
                             <property name="decimals">
                              <number>1</number>
                             </property>
                             <property name="maximum">
                              <double>999.000000000000000</double>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_30">
                             <property name="maximum">
                              <double>999.000000000000000</double>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_31"/>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_32"/>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_33"/>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_23">
                             <property name="maximum">
                              <number>999</number>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_24">
                             <property name="maximum">
                              <number>999</number>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_34">
                             <property name="maximum">
                              <double>999.000000000000000</double>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_25">
                             <property name="maximum">
                              <number>999</number>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_35">
                             <property name="decimals">
                              <number>1</number>
                             </property>
                             <property name="maximum">
                              <double>999.000000000000000</double>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_26"/>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_27"/>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_36"/>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_28"/>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_37"/>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_29"/>
                           </item>
                          </layout>
                         </widget>
                        </item>
                        <item>
                         <widget class="QWidget" name="widget_9" native="true">
                          <layout class="QVBoxLayout" name="verticalLayout_23" stretch="0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0">
                           <property name="leftMargin">
                            <number>0</number>
                           </property>
                           <property name="topMargin">
                            <number>0</number>
                           </property>
                           <property name="rightMargin">
                            <number>0</number>
                           </property>
                           <property name="bottomMargin">
                            <number>0</number>
                           </property>
                           <item>
                            <widget class="QLabel" name="label_27">
                             <property name="text">
                              <string>SV Value</string>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_39">
                             <property name="decimals">
                              <number>0</number>
                             </property>
                             <property name="maximum">
                              <double>999.000000000000000</double>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_40">
                             <property name="decimals">
                              <number>1</number>
                             </property>
                             <property name="maximum">
                              <double>999.000000000000000</double>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_41">
                             <property name="maximum">
                              <double>999.000000000000000</double>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_30">
                             <property name="maximum">
                              <number>999</number>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_31">
                             <property name="maximum">
                              <number>999</number>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_42">
                             <property name="decimals">
                              <number>1</number>
                             </property>
                             <property name="maximum">
                              <double>999.000000000000000</double>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_43">
                             <property name="maximum">
                              <double>999.000000000000000</double>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_44"/>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_45"/>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_46"/>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_32">
                             <property name="maximum">
                              <number>999</number>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_33">
                             <property name="maximum">
                              <number>999</number>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_47">
                             <property name="maximum">
                              <double>999.000000000000000</double>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_34">
                             <property name="maximum">
                              <number>999</number>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_48">
                             <property name="decimals">
                              <number>1</number>
                             </property>
                             <property name="maximum">
                              <double>999.000000000000000</double>
                             </property>
                            </widget>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_35"/>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_36"/>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_49"/>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_37"/>
                           </item>
                           <item>
                            <widget class="QDoubleSpinBox" name="doubleSpinBox_50"/>
                           </item>
                           <item>
                            <widget class="QSpinBox" name="spinBox_38"/>
                           </item>
                          </layout>
                         </widget>
                        </item>
                       </layout>
                      </widget>
                     </item>
                     <item>
                      <widget class="Line" name="line_2">
                       <property name="orientation">
                        <enum>Qt::Vertical</enum>
                       </property>
                      </widget>
                     </item>
                    </layout>
                   </widget>
                  </item>
                 </layout>
                </widget>
               </item>
              </layout>
             </widget>
            </item>
           </layout>
          </widget>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="device_tab">
       <attribute name="icon">
        <iconset>
         <normaloff>../../../../Borunte_2110A_Gui_Alter</normaloff>../../../../Borunte_2110A_Gui_Alter</iconset>
       </attribute>
       <attribute name="title">
        <string>🔧 Devices</string>
       </attribute>
       <layout class="QVBoxLayout" name="verticalLayout_17">
        <property name="spacing">
         <number>20</number>
        </property>
        <property name="leftMargin">
         <number>0</number>
        </property>
        <property name="topMargin">
         <number>0</number>
        </property>
        <property name="rightMargin">
         <number>0</number>
        </property>
        <property name="bottomMargin">
         <number>0</number>
        </property>
        <item>
         <widget class="QWidget" name="devices_container" native="true">
          <property name="sizePolicy">
           <sizepolicy hsizetype="Preferred" vsizetype="Expanding">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <layout class="QHBoxLayout" name="horizontalLayout_5" stretch="1">
           <property name="leftMargin">
            <number>0</number>
           </property>
           <property name="topMargin">
            <number>0</number>
           </property>
           <property name="rightMargin">
            <number>0</number>
           </property>
           <property name="bottomMargin">
            <number>0</number>
           </property>
           <item>
            <widget class="QFrame" name="device_frame_2">
             <property name="styleSheet">
              <string notr="true">QFrame {
    background-color: white;
    border-radius: 12px;
    border: 1px solid #E5E5E5;
    margin: 5px;
}
QFrame:hover {
    border: 1px solid #0B7EC8;
}</string>
             </property>
             <property name="frameShape">
              <enum>QFrame::NoFrame</enum>
             </property>
             <layout class="QVBoxLayout" name="verticalLayout_20" stretch="1,3,1">
              <property name="spacing">
               <number>15</number>
              </property>
              <property name="leftMargin">
               <number>20</number>
              </property>
              <property name="topMargin">
               <number>15</number>
              </property>
              <property name="rightMargin">
               <number>20</number>
              </property>
              <property name="bottomMargin">
               <number>15</number>
              </property>
              <item>
               <layout class="QHBoxLayout" name="connection_status_layout_2" stretch="1,3,2">
                <item>
                 <widget class="QLabel" name="device_icon_2">
                  <property name="styleSheet">
                   <string notr="true">font-size: 24px; 
image: url(:/newPrefix/digital.png);
color: #0B7EC8;
border: none;
</string>
                  </property>
                  <property name="text">
                   <string/>
                  </property>
                 </widget>
                </item>
                <item>
                 <layout class="QVBoxLayout" name="device_info_layout_2">
                  <property name="spacing">
                   <number>2</number>
                  </property>
                  <item>
                   <widget class="QLabel" name="name_device_label_2">
                    <property name="styleSheet">
                     <string notr="true">font-size: 16px;
font-weight: 600;
color: #1E293B;
border-radius: 10px</string>
                    </property>
                    <property name="text">
                     <string>Name:</string>
                    </property>
                   </widget>
                  </item>
                  <item>
                   <widget class="QLabel" name="type_device_label_2">
                    <property name="styleSheet">
                     <string notr="true">font-size: 14px;
color: #64748B;
border: none;</string>
                    </property>
                    <property name="text">
                     <string>Type: PLC</string>
                    </property>
                   </widget>
                  </item>
                 </layout>
                </item>
                <item>
                 <widget class="QLabel" name="status_device_label_2">
                  <property name="styleSheet">
                   <string notr="true">font-size: 12px;
font-weight: 500;
color: #EF4444;</string>
                  </property>
                  <property name="text">
                   <string>🔴 Disconnected</string>
                  </property>
                  <property name="textFormat">
                   <enum>Qt::RichText</enum>
                  </property>
                 </widget>
                </item>
               </layout>
              </item>
              <item>
               <widget class="QGroupBox" name="connection_group_2">
                <property name="styleSheet">
                 <string notr="true">QGroupBox {
    font-weight: 500;
    border: 1px solid #E5E5E5;
    border-radius: 6px;
    margin-top: 10px;
    padding-top: 10px;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px 0 5px;
    color: #374151;
}

QLabel {
	border: none;
}

QSpinBox {
    border: 1px solid #D1D5DB;
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 18px;
    background-color: #F9FAFB;
    min-width: 100px;
}
QSpinBox:focus {
    border: 2px solid #0B7EC8;
    background-color: white;
}

QLineEdit {
    border: 1px solid #D1D5DB;
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 18px;
    background-color: #F9FAFB;
}
QLineEdit:focus {
    border: 2px solid #0B7EC8;
    background-color: white;
}</string>
                </property>
                <property name="title">
                 <string>Connection Settings</string>
                </property>
                <layout class="QFormLayout" name="formLayout_2">
                 <property name="formAlignment">
                  <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
                 </property>
                 <item row="0" column="0">
                  <widget class="QLabel" name="plc_ip_address">
                   <property name="text">
                    <string>IP address:</string>
                   </property>
                  </widget>
                 </item>
                 <item row="0" column="1">
                  <widget class="QLineEdit" name="plc_ip_address_edit">
                   <property name="sizePolicy">
                    <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                     <horstretch>0</horstretch>
                     <verstretch>0</verstretch>
                    </sizepolicy>
                   </property>
                   <property name="placeholderText">
                    <string>Enter IP address: 172.16.100.///</string>
                   </property>
                  </widget>
                 </item>
                 <item row="2" column="0">
                  <widget class="QLabel" name="rack_label">
                   <property name="text">
                    <string>Rack:</string>
                   </property>
                  </widget>
                 </item>
                 <item row="2" column="1">
                  <widget class="QSpinBox" name="rack_input">
                   <property name="sizePolicy">
                    <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                     <horstretch>0</horstretch>
                     <verstretch>0</verstretch>
                    </sizepolicy>
                   </property>
                   <property name="minimumSize">
                    <size>
                     <width>126</width>
                     <height>0</height>
                    </size>
                   </property>
                   <property name="buttonSymbols">
                    <enum>QAbstractSpinBox::NoButtons</enum>
                   </property>
                  </widget>
                 </item>
                 <item row="4" column="0">
                  <widget class="QLabel" name="slot_label">
                   <property name="text">
                    <string>Slot:</string>
                   </property>
                  </widget>
                 </item>
                 <item row="4" column="1">
                  <widget class="QSpinBox" name="slot_input">
                   <property name="sizePolicy">
                    <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                     <horstretch>0</horstretch>
                     <verstretch>0</verstretch>
                    </sizepolicy>
                   </property>
                   <property name="minimumSize">
                    <size>
                     <width>126</width>
                     <height>0</height>
                    </size>
                   </property>
                   <property name="buttonSymbols">
                    <enum>QAbstractSpinBox::NoButtons</enum>
                   </property>
                   <property name="value">
                    <number>1</number>
                   </property>
                  </widget>
                 </item>
                </layout>
               </widget>
              </item>
              <item>
               <layout class="QHBoxLayout" name="connection_btn_layout_2">
                <item>
                 <widget class="QPushButton" name="plc_connect">
                  <property name="sizePolicy">
                   <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                    <horstretch>0</horstretch>
                    <verstretch>0</verstretch>
                   </sizepolicy>
                  </property>
                  <property name="styleSheet">
                   <string notr="true">QPushButton {
    background-color: #10B981;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
}
QPushButton:hover {
    background-color: #059669;
}</string>
                  </property>
                  <property name="text">
                   <string>🔌 Connect</string>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QPushButton" name="dis_plc">
                  <property name="sizePolicy">
                   <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                    <horstretch>0</horstretch>
                    <verstretch>0</verstretch>
                   </sizepolicy>
                  </property>
                  <property name="styleSheet">
                   <string notr="true">QPushButton {
    background-color: #EF4444;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
}
QPushButton:hover {
    background-color: #DC2626;
}</string>
                  </property>
                  <property name="text">
                   <string>⛓️‍💥 Disconnect</string>
                  </property>
                 </widget>
                </item>
               </layout>
              </item>
             </layout>
            </widget>
           </item>
          </layout>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="dashboard_tab">
       <attribute name="icon">
        <iconset>
         <normaloff>../../../../Borunte_2110A_Gui_Alter</normaloff>../../../../Borunte_2110A_Gui_Alter</iconset>
       </attribute>
       <attribute name="title">
        <string>📊 Dashboard</string>
       </attribute>
       <layout class="QVBoxLayout" name="verticalLayout_3">
        <property name="leftMargin">
         <number>15</number>
        </property>
        <property name="topMargin">
         <number>15</number>
        </property>
        <property name="rightMargin">
         <number>15</number>
        </property>
        <property name="bottomMargin">
         <number>15</number>
        </property>
        <item>
         <widget class="QStackedWidget" name="dashboard_stacked_widget">
          <property name="currentIndex">
           <number>1</number>
          </property>
          <widget class="QWidget" name="overall_page">
           <layout class="QVBoxLayout" name="verticalLayout_12">
            <property name="leftMargin">
             <number>0</number>
            </property>
            <property name="topMargin">
             <number>0</number>
            </property>
            <property name="rightMargin">
             <number>0</number>
            </property>
            <property name="bottomMargin">
             <number>0</number>
            </property>
            <item>
             <widget class="QWidget" name="card_widgets" native="true">
              <property name="sizePolicy">
               <sizepolicy hsizetype="Preferred" vsizetype="Expanding">
                <horstretch>0</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="styleSheet">
               <string notr="true">QFrame {
    background-color: white;
    border-radius: 5px;
    border: 1px solid #E5E5E5;
    
}
QFrame:hover {
    border: 1px solid #0B7EC8;
    
}</string>
              </property>
              <layout class="QGridLayout" name="gridLayout" rowstretch="1,5" columnstretch="1,1">
               <property name="leftMargin">
                <number>10</number>
               </property>
               <property name="topMargin">
                <number>10</number>
               </property>
               <property name="rightMargin">
                <number>10</number>
               </property>
               <property name="bottomMargin">
                <number>10</number>
               </property>
               <property name="spacing">
                <number>15</number>
               </property>
               <item row="1" column="0">
                <widget class="QFrame" name="card_frame">
                 <property name="styleSheet">
                  <string notr="true">QPushButton {
    background-color: #0B7EC8;
    color: white;
    border: none;
    padding: 8px 18px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 500;
}
QPushButton:hover {
    background-color: #0968A3;
}</string>
                 </property>
                 <property name="frameShape">
                  <enum>QFrame::NoFrame</enum>
                 </property>
                 <layout class="QVBoxLayout" name="verticalLayout_8" stretch="5,1">
                  <property name="spacing">
                   <number>5</number>
                  </property>
                  <property name="leftMargin">
                   <number>10</number>
                  </property>
                  <property name="topMargin">
                   <number>10</number>
                  </property>
                  <property name="rightMargin">
                   <number>10</number>
                  </property>
                  <property name="bottomMargin">
                   <number>10</number>
                  </property>
                  <item>
                   <layout class="QVBoxLayout" name="card_content"/>
                  </item>
                  <item>
                   <layout class="QHBoxLayout" name="horizontalLayout_17">
                    <item alignment="Qt::AlignHCenter">
                     <widget class="QLabel" name="card_label">
                      <property name="styleSheet">
                       <string notr="true">font-size: 14px;
color: #555555;
font-weight: 500;
margin-top: 8px;
border: none;</string>
                      </property>
                      <property name="text">
                       <string> Unit of Weekdays</string>
                      </property>
                     </widget>
                    </item>
                    <item alignment="Qt::AlignRight">
                     <widget class="QPushButton" name="card_btn">
                      <property name="sizePolicy">
                       <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                        <horstretch>0</horstretch>
                        <verstretch>0</verstretch>
                       </sizepolicy>
                      </property>
                      <property name="minimumSize">
                       <size>
                        <width>0</width>
                        <height>0</height>
                       </size>
                      </property>
                      <property name="styleSheet">
                       <string notr="true"/>
                      </property>
                      <property name="text">
                       <string>🔍View Details</string>
                      </property>
                     </widget>
                    </item>
                   </layout>
                  </item>
                 </layout>
                </widget>
               </item>
               <item row="1" column="1">
                <widget class="QFrame" name="card_frame_2">
                 <property name="styleSheet">
                  <string notr="true">QPushButton {
    background-color: #0B7EC8;
    color: white;
    border: none;
    padding: 8px 18px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 500;
}
QPushButton:hover {
    background-color: #0968A3;
}</string>
                 </property>
                 <property name="frameShape">
                  <enum>QFrame::NoFrame</enum>
                 </property>
                 <layout class="QVBoxLayout" name="verticalLayout_9" stretch="5,1">
                  <property name="spacing">
                   <number>5</number>
                  </property>
                  <property name="leftMargin">
                   <number>10</number>
                  </property>
                  <property name="topMargin">
                   <number>10</number>
                  </property>
                  <property name="rightMargin">
                   <number>10</number>
                  </property>
                  <property name="bottomMargin">
                   <number>10</number>
                  </property>
                  <item>
                   <layout class="QVBoxLayout" name="card_content_2"/>
                  </item>
                  <item>
                   <layout class="QHBoxLayout" name="horizontalLayout_16">
                    <item alignment="Qt::AlignHCenter">
                     <widget class="QLabel" name="card_label_2">
                      <property name="styleSheet">
                       <string notr="true">font-size: 14px;
color: #555555;
font-weight: 500;
margin-top: 8px;
border: none;</string>
                      </property>
                      <property name="text">
                       <string> Issue of Weekdays</string>
                      </property>
                     </widget>
                    </item>
                    <item alignment="Qt::AlignRight">
                     <widget class="QPushButton" name="card_btn_2">
                      <property name="sizePolicy">
                       <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                        <horstretch>0</horstretch>
                        <verstretch>0</verstretch>
                       </sizepolicy>
                      </property>
                      <property name="minimumSize">
                       <size>
                        <width>0</width>
                        <height>0</height>
                       </size>
                      </property>
                      <property name="styleSheet">
                       <string notr="true"/>
                      </property>
                      <property name="text">
                       <string>🔍View Details</string>
                      </property>
                     </widget>
                    </item>
                   </layout>
                  </item>
                 </layout>
                </widget>
               </item>
               <item row="0" column="0" colspan="2">
                <widget class="QFrame" name="stats_frame">
                 <property name="styleSheet">
                  <string notr="true">QFrame {
    background-color: white;
    border-radius: 12px;
    border: 1px solid #E5E5E5;
}
alignment: right;</string>
                 </property>
                 <property name="frameShape">
                  <enum>QFrame::NoFrame</enum>
                 </property>
                 <layout class="QHBoxLayout" name="horizontalLayout_2">
                  <property name="leftMargin">
                   <number>0</number>
                  </property>
                  <property name="topMargin">
                   <number>10</number>
                  </property>
                  <property name="rightMargin">
                   <number>0</number>
                  </property>
                  <property name="bottomMargin">
                   <number>10</number>
                  </property>
                  <item>
                   <widget class="QWidget" name="stats_widget" native="true">
                    <layout class="QVBoxLayout" name="verticalLayout_7">
                     <property name="leftMargin">
                      <number>15</number>
                     </property>
                     <property name="topMargin">
                      <number>15</number>
                     </property>
                     <property name="rightMargin">
                      <number>15</number>
                     </property>
                     <property name="bottomMargin">
                      <number>15</number>
                     </property>
                     <item>
                      <widget class="QPushButton" name="value_label">
                       <property name="text">
                        <string>0</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="unit_label">
                       <property name="styleSheet">
                        <string notr="true">font-size: 13px;
color: #888888;
font-weight: 500;
border: none;</string>
                       </property>
                       <property name="text">
                        <string>units/day</string>
                       </property>
                       <property name="alignment">
                        <set>Qt::AlignCenter</set>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="title_label_stats">
                       <property name="styleSheet">
                        <string notr="true">font-size: 14px;
color: #555555;
font-weight: 500;
margin-top: 8px;
border: none;</string>
                       </property>
                       <property name="text">
                        <string>Production Output</string>
                       </property>
                       <property name="alignment">
                        <set>Qt::AlignCenter</set>
                       </property>
                      </widget>
                     </item>
                    </layout>
                   </widget>
                  </item>
                  <item>
                   <widget class="QWidget" name="stats_widget_2" native="true">
                    <layout class="QVBoxLayout" name="verticalLayout_6">
                     <property name="leftMargin">
                      <number>15</number>
                     </property>
                     <property name="topMargin">
                      <number>15</number>
                     </property>
                     <property name="rightMargin">
                      <number>15</number>
                     </property>
                     <property name="bottomMargin">
                      <number>15</number>
                     </property>
                     <item>
                      <widget class="QPushButton" name="value_label_2">
                       <property name="text">
                        <string>0</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="unit_label_2">
                       <property name="styleSheet">
                        <string notr="true">font-size: 13px;
color: #888888;
font-weight: 500;
border: none;</string>
                       </property>
                       <property name="text">
                        <string>issues</string>
                       </property>
                       <property name="alignment">
                        <set>Qt::AlignCenter</set>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="title_label_stats_2">
                       <property name="styleSheet">
                        <string notr="true">font-size: 14px;
color: #555555;
font-weight: 500;
margin-top: 8px;
border: none;</string>
                       </property>
                       <property name="text">
                        <string>Issues Today</string>
                       </property>
                       <property name="alignment">
                        <set>Qt::AlignCenter</set>
                       </property>
                      </widget>
                     </item>
                    </layout>
                   </widget>
                  </item>
                  <item>
                   <widget class="QWidget" name="stats_widget_3" native="true">
                    <layout class="QVBoxLayout" name="verticalLayout_5">
                     <property name="leftMargin">
                      <number>15</number>
                     </property>
                     <property name="topMargin">
                      <number>15</number>
                     </property>
                     <property name="rightMargin">
                      <number>15</number>
                     </property>
                     <property name="bottomMargin">
                      <number>15</number>
                     </property>
                     <item>
                      <widget class="QPushButton" name="value_label_3">
                       <property name="text">
                        <string>0</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="unit_label_3">
                       <property name="styleSheet">
                        <string notr="true">font-size: 13px;
color: #888888;
font-weight: 500;
border: none;</string>
                       </property>
                       <property name="text">
                        <string> min/unit</string>
                       </property>
                       <property name="alignment">
                        <set>Qt::AlignCenter</set>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="title_label_stats_3">
                       <property name="styleSheet">
                        <string notr="true">font-size: 14px;
color: #555555;
font-weight: 500;
margin-top: 8px;
border: none;</string>
                       </property>
                       <property name="text">
                        <string>Cycle Time</string>
                       </property>
                       <property name="alignment">
                        <set>Qt::AlignCenter</set>
                       </property>
                      </widget>
                     </item>
                    </layout>
                   </widget>
                  </item>
                  <item>
                   <widget class="QWidget" name="stats_widget_4" native="true">
                    <layout class="QVBoxLayout" name="verticalLayout_4">
                     <property name="leftMargin">
                      <number>15</number>
                     </property>
                     <property name="topMargin">
                      <number>15</number>
                     </property>
                     <property name="rightMargin">
                      <number>15</number>
                     </property>
                     <property name="bottomMargin">
                      <number>15</number>
                     </property>
                     <item>
                      <widget class="QPushButton" name="value_label_4">
                       <property name="text">
                        <string>0</string>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="unit_label_4">
                       <property name="styleSheet">
                        <string notr="true">font-size: 13px;
color: #888888;
font-weight: 500;
border: none;</string>
                       </property>
                       <property name="text">
                        <string>time</string>
                       </property>
                       <property name="alignment">
                        <set>Qt::AlignCenter</set>
                       </property>
                      </widget>
                     </item>
                     <item>
                      <widget class="QLabel" name="title_label_stats_4">
                       <property name="styleSheet">
                        <string notr="true">font-size: 14px;
color: #555555;
font-weight: 500;
margin-top: 8px;
border: none;</string>
                       </property>
                       <property name="text">
                        <string>Working Time</string>
                       </property>
                       <property name="alignment">
                        <set>Qt::AlignCenter</set>
                       </property>
                      </widget>
                     </item>
                    </layout>
                   </widget>
                  </item>
                 </layout>
                </widget>
               </item>
              </layout>
             </widget>
            </item>
           </layout>
          </widget>
          <widget class="QWidget" name="list_page">
           <layout class="QVBoxLayout" name="verticalLayout_13">
            <property name="leftMargin">
             <number>0</number>
            </property>
            <property name="topMargin">
             <number>0</number>
            </property>
            <property name="rightMargin">
             <number>0</number>
            </property>
            <property name="bottomMargin">
             <number>0</number>
            </property>
            <item>
             <widget class="QStackedWidget" name="stackedWidget">
              <widget class="QWidget" name="list_err_page">
               <layout class="QVBoxLayout" name="verticalLayout_54">
                <property name="spacing">
                 <number>0</number>
                </property>
                <property name="leftMargin">
                 <number>0</number>
                </property>
                <property name="topMargin">
                 <number>0</number>
                </property>
                <property name="rightMargin">
                 <number>0</number>
                </property>
                <property name="bottomMargin">
                 <number>0</number>
                </property>
               </layout>
              </widget>
              <widget class="QWidget" name="list_done_page">
               <layout class="QVBoxLayout" name="verticalLayout_55">
                <property name="spacing">
                 <number>0</number>
                </property>
                <property name="leftMargin">
                 <number>0</number>
                </property>
                <property name="topMargin">
                 <number>0</number>
                </property>
                <property name="rightMargin">
                 <number>0</number>
                </property>
                <property name="bottomMargin">
                 <number>0</number>
                </property>
                <item>
                 <widget class="QTableWidget" name="list_done">
                  <property name="sizePolicy">
                   <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
                    <horstretch>0</horstretch>
                    <verstretch>0</verstretch>
                   </sizepolicy>
                  </property>
                  <property name="palette">
                   <palette>
                    <active>
                     <colorrole role="WindowText">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>0</red>
                        <green>0</green>
                        <blue>0</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="Button">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>255</red>
                        <green>252</green>
                        <blue>253</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="Text">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>0</red>
                        <green>0</green>
                        <blue>0</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="ButtonText">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>0</red>
                        <green>0</green>
                        <blue>0</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="Base">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>255</red>
                        <green>252</green>
                        <blue>253</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="Window">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>255</red>
                        <green>252</green>
                        <blue>253</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="PlaceholderText">
                      <brush brushstyle="NoBrush">
                       <color alpha="128">
                        <red>0</red>
                        <green>0</green>
                        <blue>0</blue>
                       </color>
                      </brush>
                     </colorrole>
                    </active>
                    <inactive>
                     <colorrole role="WindowText">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>0</red>
                        <green>0</green>
                        <blue>0</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="Button">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>255</red>
                        <green>252</green>
                        <blue>253</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="Text">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>0</red>
                        <green>0</green>
                        <blue>0</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="ButtonText">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>0</red>
                        <green>0</green>
                        <blue>0</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="Base">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>255</red>
                        <green>252</green>
                        <blue>253</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="Window">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>255</red>
                        <green>252</green>
                        <blue>253</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="PlaceholderText">
                      <brush brushstyle="NoBrush">
                       <color alpha="128">
                        <red>0</red>
                        <green>0</green>
                        <blue>0</blue>
                       </color>
                      </brush>
                     </colorrole>
                    </inactive>
                    <disabled>
                     <colorrole role="WindowText">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>0</red>
                        <green>0</green>
                        <blue>0</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="Button">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>255</red>
                        <green>252</green>
                        <blue>253</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="Text">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>0</red>
                        <green>0</green>
                        <blue>0</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="ButtonText">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>0</red>
                        <green>0</green>
                        <blue>0</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="Base">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>255</red>
                        <green>252</green>
                        <blue>253</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="Window">
                      <brush brushstyle="SolidPattern">
                       <color alpha="255">
                        <red>255</red>
                        <green>252</green>
                        <blue>253</blue>
                       </color>
                      </brush>
                     </colorrole>
                     <colorrole role="PlaceholderText">
                      <brush brushstyle="NoBrush">
                       <color alpha="128">
                        <red>0</red>
                        <green>0</green>
                        <blue>0</blue>
                       </color>
                      </brush>
                     </colorrole>
                    </disabled>
                   </palette>
                  </property>
                  <property name="styleSheet">
                   <string notr="true">QTableWidget {	
	color: rgb(0, 0, 0);
	background-color: rgb(255, 252, 253);
	padding: 10px;
	border-radius: 5px;
	gridline-color: rgb(44, 49, 60);
	border-bottom: 1px solid rgb(44, 49, 60);
	
}
QTableWidget::item{
	border-color: rgb(44, 49, 60);
	padding-left: 5px;
	padding-right: 5px;
	gridline-color: rgb(44, 49, 60);
}
QTableWidget::item:hover{
	background-color: rgb(85, 170, 255);
}
QScrollArea {
    border: none;
    background-color: transparent;
}
QScrollBar:vertical {
    border: none;
    background-color: #F1F5F9;
    width: 10px;
    border-radius: 5px;
}
QScrollBar::handle:vertical {
    background-color: #CBD5E1;
    border-radius: 5px;
    min-height: 30px;
}
QScrollBar::handle:vertical:hover {
    background-color: #94A3B8;
}

QScrollBar:horizontal
{
    border: none;
    background-color: #F1F5F9;
    height: 10px;
    border-radius: 5px;
}
QScrollBar::handle:horizontal {
    background-color: #CBD5E1;
    border-radius: 5px;
    min-height: 30px;
}
QScrollBar::handle:horizontal:hover {
    background-color: #94A3B8;
}
QHeaderView::section{
	Background-color: rgb(39, 44, 54);
	max-width: 30px;
	border: 1px solid rgb(44, 49, 60);
	border-style: none;
    border-bottom: 1px solid rgb(44, 49, 60);
    border-right: 1px solid rgb(44, 49, 60);
}
QTableWidget::horizontalHeader {	
	background-color: rgb(81, 255, 0);
}
QHeaderView::section:horizontal
{
    border: 1px solid rgb(32, 34, 42);
	background-color: rgb(27, 29, 35);
	padding: 3px;
	border-top-left-radius: 7px;
    border-top-right-radius: 7px;
}
QHeaderView::section:vertical
{
    border: 1px solid rgb(44, 49, 60);
}
</string>
                  </property>
                  <property name="frameShape">
                   <enum>QFrame::NoFrame</enum>
                  </property>
                  <property name="verticalScrollBarPolicy">
                   <enum>Qt::ScrollBarAlwaysOn</enum>
                  </property>
                  <property name="sizeAdjustPolicy">
                   <enum>QAbstractScrollArea::AdjustToContents</enum>
                  </property>
                  <property name="editTriggers">
                   <set>QAbstractItemView::NoEditTriggers</set>
                  </property>
                  <property name="alternatingRowColors">
                   <bool>false</bool>
                  </property>
                  <property name="selectionMode">
                   <enum>QAbstractItemView::NoSelection</enum>
                  </property>
                  <property name="selectionBehavior">
                   <enum>QAbstractItemView::SelectRows</enum>
                  </property>
                  <property name="showGrid">
                   <bool>true</bool>
                  </property>
                  <property name="gridStyle">
                   <enum>Qt::SolidLine</enum>
                  </property>
                  <property name="sortingEnabled">
                   <bool>false</bool>
                  </property>
                  <attribute name="horizontalHeaderVisible">
                   <bool>false</bool>
                  </attribute>
                  <attribute name="horizontalHeaderCascadingSectionResizes">
                   <bool>true</bool>
                  </attribute>
                  <attribute name="horizontalHeaderDefaultSectionSize">
                   <number>150</number>
                  </attribute>
                  <attribute name="horizontalHeaderStretchLastSection">
                   <bool>true</bool>
                  </attribute>
                  <attribute name="verticalHeaderVisible">
                   <bool>false</bool>
                  </attribute>
                  <attribute name="verticalHeaderCascadingSectionResizes">
                   <bool>false</bool>
                  </attribute>
                  <attribute name="verticalHeaderMinimumSectionSize">
                   <number>30</number>
                  </attribute>
                  <attribute name="verticalHeaderDefaultSectionSize">
                   <number>40</number>
                  </attribute>
                  <attribute name="verticalHeaderHighlightSections">
                   <bool>false</bool>
                  </attribute>
                  <attribute name="verticalHeaderStretchLastSection">
                   <bool>true</bool>
                  </attribute>
                  <row>
                   <property name="text">
                    <string>1</string>
                   </property>
                   <property name="font">
                    <font>
                     <family>Segoe UI</family>
                    </font>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>2</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>3</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>4</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>5</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>6</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>7</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>8</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>9</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>10</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>11</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>12</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>14</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>15</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>16</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>17</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>18</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>19</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>20</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>21</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>22</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>23</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>24</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>25</string>
                   </property>
                  </row>
                  <row>
                   <property name="text">
                    <string>26</string>
                   </property>
                  </row>
                  <column>
                   <property name="text">
                    <string notr="true">0</string>
                   </property>
                   <property name="toolTip">
                    <string notr="true"/>
                   </property>
                   <property name="whatsThis">
                    <string notr="true"/>
                   </property>
                  </column>
                  <column>
                   <property name="text">
                    <string notr="true">1</string>
                   </property>
                  </column>
                  <column>
                   <property name="text">
                    <string notr="true">2</string>
                   </property>
                  </column>
                  <column>
                   <property name="text">
                    <string notr="true">3</string>
                   </property>
                  </column>
                  <column>
                   <property name="text">
                    <string>4</string>
                   </property>
                  </column>
                  <column>
                   <property name="text">
                    <string>5</string>
                   </property>
                  </column>
                  <column>
                   <property name="text">
                    <string>6</string>
                   </property>
                  </column>
                  <column>
                   <property name="text">
                    <string>7</string>
                   </property>
                  </column>
                  <column>
                   <property name="text">
                    <string>8</string>
                   </property>
                  </column>
                  <item row="0" column="0">
                   <property name="text">
                    <string notr="true">No.</string>
                   </property>
                   <property name="toolTip">
                    <string notr="true"/>
                   </property>
                   <property name="whatsThis">
                    <string notr="true"/>
                   </property>
                   <property name="font">
                    <font>
                     <weight>75</weight>
                     <bold>true</bold>
                    </font>
                   </property>
                  </item>
                  <item row="0" column="1">
                   <property name="text">
                    <string>Type.</string>
                   </property>
                   <property name="font">
                    <font>
                     <weight>75</weight>
                     <bold>true</bold>
                    </font>
                   </property>
                  </item>
                  <item row="0" column="2">
                   <property name="text">
                    <string>Start.</string>
                   </property>
                   <property name="font">
                    <font>
                     <weight>75</weight>
                     <bold>true</bold>
                    </font>
                   </property>
                  </item>
                  <item row="0" column="3">
                   <property name="text">
                    <string>Done.</string>
                   </property>
                   <property name="font">
                    <font>
                     <weight>75</weight>
                     <bold>true</bold>
                    </font>
                   </property>
                  </item>
                  <item row="0" column="4">
                   <property name="text">
                    <string>Total Time.</string>
                   </property>
                   <property name="font">
                    <font>
                     <weight>75</weight>
                     <bold>true</bold>
                    </font>
                   </property>
                  </item>
                  <item row="0" column="5">
                   <property name="text">
                    <string>Date.</string>
                   </property>
                   <property name="font">
                    <font>
                     <weight>75</weight>
                     <bold>true</bold>
                    </font>
                   </property>
                  </item>
                  <item row="0" column="6">
                   <property name="text">
                    <string>Total Length.</string>
                   </property>
                   <property name="font">
                    <font>
                     <weight>75</weight>
                     <bold>true</bold>
                    </font>
                   </property>
                  </item>
                  <item row="0" column="7">
                   <property name="text">
                    <string>Total Weight.</string>
                   </property>
                   <property name="font">
                    <font>
                     <weight>75</weight>
                     <bold>true</bold>
                    </font>
                   </property>
                  </item>
                  <item row="0" column="8">
                   <property name="text">
                    <string>Speed.</string>
                   </property>
                   <property name="font">
                    <font>
                     <weight>75</weight>
                     <bold>true</bold>
                    </font>
                   </property>
                  </item>
                 </widget>
                </item>
               </layout>
              </widget>
             </widget>
            </item>
            <item>
             <layout class="QHBoxLayout" name="list_query_btn">
              <item>
               <widget class="QPushButton" name="next_page_btn">
                <property name="sizePolicy">
                 <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                  <horstretch>0</horstretch>
                  <verstretch>0</verstretch>
                 </sizepolicy>
                </property>
                <property name="styleSheet">
                 <string notr="true">QPushButton {
    background-color: white;
    color: #0B7EC8;
    border: 1px solid #0B7EC8;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
}
QPushButton:hover {
    background-color: #F0F9FF;
}
QPushButton:pressed {
    background-color: #E0F2FE;
}</string>
                </property>
                <property name="text">
                 <string>⬅️ Next Page</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QPushButton" name="backward_btn">
                <property name="sizePolicy">
                 <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                  <horstretch>0</horstretch>
                  <verstretch>0</verstretch>
                 </sizepolicy>
                </property>
                <property name="styleSheet">
                 <string notr="true">QPushButton {
    background-color: white;
    color: #0B7EC8;
    border: 1px solid #0B7EC8;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
}
QPushButton:hover {
    background-color: #F0F9FF;
}
QPushButton:pressed {
    background-color: #E0F2FE;
}</string>
                </property>
                <property name="text">
                 <string>📈 Go Back</string>
                </property>
               </widget>
              </item>
             </layout>
            </item>
           </layout>
          </widget>
         </widget>
        </item>
       </layout>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources>
  <include location="../../../../../Pictures/QT_Icon/Icon.qrc"/>
  <include location="../../../Simple_PySide_Base-master/Simple_PySide_Base-master/files.qrc"/>
 </resources>
 <connections/>
</ui>
