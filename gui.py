<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1291</width>
    <height>816</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(235, 235, 235);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout_3">
    <item>
     <widget class="QFrame" name="Titre_frame">
      <property name="minimumSize">
       <size>
        <width>0</width>
        <height>101</height>
       </size>
      </property>
      <property name="maximumSize">
       <size>
        <width>16777215</width>
        <height>101</height>
       </size>
      </property>
      <property name="frameShape">
       <enum>QFrame::StyledPanel</enum>
      </property>
      <property name="frameShadow">
       <enum>QFrame::Raised</enum>
      </property>
      <layout class="QHBoxLayout" name="horizontalLayout">
       <item>
        <widget class="QLabel" name="Title">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>                       Bienvenu sur la base de données émmisions CO2 Voiture immatréculées en france </string>
         </property>
         <property name="alignment">
          <set>Qt::AlignCenter</set>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QFrame" name="Titre_bouton">
         <property name="minimumSize">
          <size>
           <width>121</width>
           <height>41</height>
          </size>
         </property>
         <property name="maximumSize">
          <size>
           <width>121</width>
           <height>41</height>
          </size>
         </property>
         <property name="frameShape">
          <enum>QFrame::StyledPanel</enum>
         </property>
         <property name="frameShadow">
          <enum>QFrame::Raised</enum>
         </property>
         <widget class="QPushButton" name="minimizeButton">
          <property name="geometry">
           <rect>
            <x>10</x>
            <y>10</y>
            <width>25</width>
            <height>24</height>
           </rect>
          </property>
          <property name="cursor">
           <cursorShape>PointingHandCursor</cursorShape>
          </property>
          <property name="whatsThis">
           <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
          </property>
          <property name="styleSheet">
           <string notr="true">background-color: rgb(84, 84, 126);</string>
          </property>
          <property name="text">
           <string/>
          </property>
          <property name="icon">
           <iconset resource="E:/EDF/new_app/icons.qrc">
            <normaloff>:/icons/icons/cil-minus.png</normaloff>:/icons/icons/cil-minus.png</iconset>
          </property>
          <property name="iconSize">
           <size>
            <width>24</width>
            <height>24</height>
           </size>
          </property>
         </widget>
         <widget class="QPushButton" name="closeButton">
          <property name="geometry">
           <rect>
            <x>84</x>
            <y>10</y>
            <width>24</width>
            <height>24</height>
           </rect>
          </property>
          <property name="cursor">
           <cursorShape>PointingHandCursor</cursorShape>
          </property>
          <property name="styleSheet">
           <string notr="true">background-repeat: none;
background-position: center left;
background-image: url(:/icons/icons/cil-x.png);
background-color: rgb(84, 84, 126);
</string>
          </property>
          <property name="text">
           <string/>
          </property>
          <property name="icon">
           <iconset resource="E:/EDF/new_app/icons.qrc">
            <normaloff>:/icons/icons/cil-x.png</normaloff>:/icons/icons/cil-x.png</iconset>
          </property>
          <property name="iconSize">
           <size>
            <width>24</width>
            <height>24</height>
           </size>
          </property>
         </widget>
         <widget class="QPushButton" name="restoreButton">
          <property name="geometry">
           <rect>
            <x>47</x>
            <y>10</y>
            <width>25</width>
            <height>24</height>
           </rect>
          </property>
          <property name="cursor">
           <cursorShape>PointingHandCursor</cursorShape>
          </property>
          <property name="styleSheet">
           <string notr="true">background-image: url(:/icons/icons/cil-window-maximize.png);
background-repeat: none;
background-position: center left;
background-color: rgb(84, 84, 126);
</string>
          </property>
          <property name="text">
           <string/>
          </property>
          <property name="icon">
           <iconset resource="E:/EDF/new_app/icons.qrc">
            <normaloff>:/icons/icons/cil-window-maximize.png</normaloff>:/icons/icons/cil-window-maximize.png</iconset>
          </property>
          <property name="iconSize">
           <size>
            <width>24</width>
            <height>24</height>
           </size>
          </property>
         </widget>
        </widget>
       </item>
      </layout>
     </widget>
    </item>
    <item>
     <widget class="QStackedWidget" name="stackedWidget">
      <property name="styleSheet">
       <string notr="true"/>
      </property>
      <property name="currentIndex">
       <number>1</number>
      </property>
      <widget class="QWidget" name="Database_config">
       <layout class="QVBoxLayout" name="verticalLayout">
        <item>
         <widget class="QFrame" name="frame_3">
          <property name="styleSheet">
           <string notr="true"/>
          </property>
          <property name="frameShape">
           <enum>QFrame::StyledPanel</enum>
          </property>
          <property name="frameShadow">
           <enum>QFrame::Raised</enum>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QFrame" name="frame_4">
          <property name="minimumSize">
           <size>
            <width>0</width>
            <height>600</height>
           </size>
          </property>
          <property name="maximumSize">
           <size>
            <width>16777215</width>
            <height>600</height>
           </size>
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
          <layout class="QHBoxLayout" name="horizontalLayout_2">
           <item>
            <widget class="QFrame" name="frame_7">
             <property name="minimumSize">
              <size>
               <width>0</width>
               <height>550</height>
              </size>
             </property>
             <property name="maximumSize">
              <size>
               <width>16777215</width>
               <height>550</height>
              </size>
             </property>
             <property name="styleSheet">
              <string notr="true">background-color: none;</string>
             </property>
             <property name="frameShape">
              <enum>QFrame::StyledPanel</enum>
             </property>
             <property name="frameShadow">
              <enum>QFrame::Raised</enum>
             </property>
            </widget>
           </item>
           <item>
            <widget class="QFrame" name="frame_6">
             <property name="minimumSize">
              <size>
               <width>680</width>
               <height>550</height>
              </size>
             </property>
             <property name="maximumSize">
              <size>
               <width>680</width>
               <height>550</height>
              </size>
             </property>
             <property name="styleSheet">
              <string notr="true">QFrame{
	
	background-color: rgb(218, 218, 218);
}
QPushButton{
	padding: 20px 10px;
	border: none;
	border-left: 2px solid transparent;
	border-bottom: 2px solid transparent;
	border-radius: 5px;
	background-color: rgb(68, 68, 102);
	color: rgb(140, 140, 140);
}
QPushButton:hover{
	background-color: rgb(0, 92, 157);
}
QPushButton:pressed {
	background-color:  rgb(0, 92, 157);
	border-bottom: 2px solid rgb(255, 165, 24);
}</string>
             </property>
             <property name="frameShape">
              <enum>QFrame::StyledPanel</enum>
             </property>
             <property name="frameShadow">
              <enum>QFrame::Raised</enum>
             </property>
             <widget class="QLabel" name="label_4">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>34</y>
                <width>653</width>
                <height>157</height>
               </rect>
              </property>
              <property name="font">
               <font>
                <pointsize>12</pointsize>
               </font>
              </property>
              <property name="text">
               <string>Database Configuration</string>
              </property>
              <property name="alignment">
               <set>Qt::AlignCenter</set>
              </property>
             </widget>
             <widget class="QFrame" name="frame_14">
              <property name="geometry">
               <rect>
                <x>340</x>
                <y>360</y>
                <width>323</width>
                <height>157</height>
               </rect>
              </property>
              <property name="frameShape">
               <enum>QFrame::StyledPanel</enum>
              </property>
              <property name="frameShadow">
               <enum>QFrame::Raised</enum>
              </property>
              <widget class="QPushButton" name="valid_config">
               <property name="geometry">
                <rect>
                 <x>150</x>
                 <y>30</y>
                 <width>111</width>
                 <height>31</height>
                </rect>
               </property>
               <property name="text">
                <string>Validation</string>
               </property>
              </widget>
              <widget class="QPushButton" name="cancel_config">
               <property name="geometry">
                <rect>
                 <x>20</x>
                 <y>30</y>
                 <width>111</width>
                 <height>31</height>
                </rect>
               </property>
               <property name="text">
                <string>Previous</string>
               </property>
              </widget>
             </widget>
             <widget class="QFrame" name="frame_13">
              <property name="geometry">
               <rect>
                <x>340</x>
                <y>197</y>
                <width>323</width>
                <height>157</height>
               </rect>
              </property>
              <property name="frameShape">
               <enum>QFrame::StyledPanel</enum>
              </property>
              <property name="frameShadow">
               <enum>QFrame::Raised</enum>
              </property>
              <widget class="QLineEdit" name="Database_name">
               <property name="geometry">
                <rect>
                 <x>20</x>
                 <y>60</y>
                 <width>211</width>
                 <height>31</height>
                </rect>
               </property>
               <property name="styleSheet">
                <string notr="true">background-color: rgb(207, 219, 255);
color: rgb(182, 60, 182);
font: 12pt &quot;Century Gothic&quot;;</string>
               </property>
              </widget>
             </widget>
             <widget class="QFrame" name="frame_15">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>197</y>
                <width>324</width>
                <height>157</height>
               </rect>
              </property>
              <property name="frameShape">
               <enum>QFrame::StyledPanel</enum>
              </property>
              <property name="frameShadow">
               <enum>QFrame::Raised</enum>
              </property>
              <widget class="QLabel" name="label_117">
               <property name="geometry">
                <rect>
                 <x>40</x>
                 <y>60</y>
                 <width>231</width>
                 <height>31</height>
                </rect>
               </property>
               <property name="styleSheet">
                <string notr="true">color: rgb(0, 0, 0);
font: 16pt &quot;Century Gothic&quot;;</string>
               </property>
               <property name="text">
                <string>Database name</string>
               </property>
              </widget>
             </widget>
             <widget class="QFrame" name="frame_16">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>360</y>
                <width>324</width>
                <height>157</height>
               </rect>
              </property>
              <property name="frameShape">
               <enum>QFrame::StyledPanel</enum>
              </property>
              <property name="frameShadow">
               <enum>QFrame::Raised</enum>
              </property>
             </widget>
            </widget>
           </item>
           <item>
            <widget class="QFrame" name="frame_8">
             <property name="minimumSize">
              <size>
               <width>0</width>
               <height>550</height>
              </size>
             </property>
             <property name="maximumSize">
              <size>
               <width>16777215</width>
               <height>550</height>
              </size>
             </property>
             <property name="styleSheet">
              <string notr="true">background-color: none;</string>
             </property>
             <property name="frameShape">
              <enum>QFrame::StyledPanel</enum>
             </property>
             <property name="frameShadow">
              <enum>QFrame::Raised</enum>
             </property>
            </widget>
           </item>
          </layout>
         </widget>
        </item>
        <item>
         <widget class="QFrame" name="frame_5">
          <property name="styleSheet">
           <string notr="true"/>
          </property>
          <property name="frameShape">
           <enum>QFrame::StyledPanel</enum>
          </property>
          <property name="frameShadow">
           <enum>QFrame::Raised</enum>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="Connect_server">
       <layout class="QVBoxLayout" name="verticalLayout_2">
        <item>
         <widget class="QFrame" name="frame_28">
          <property name="styleSheet">
           <string notr="true"/>
          </property>
          <property name="frameShape">
           <enum>QFrame::StyledPanel</enum>
          </property>
          <property name="frameShadow">
           <enum>QFrame::Raised</enum>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QFrame" name="frame_18">
          <property name="minimumSize">
           <size>
            <width>0</width>
            <height>600</height>
           </size>
          </property>
          <property name="maximumSize">
           <size>
            <width>16777215</width>
            <height>600</height>
           </size>
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
          <layout class="QHBoxLayout" name="horizontalLayout_3">
           <item>
            <widget class="QFrame" name="frame_19">
             <property name="minimumSize">
              <size>
               <width>0</width>
               <height>550</height>
              </size>
             </property>
             <property name="maximumSize">
              <size>
               <width>16777215</width>
               <height>550</height>
              </size>
             </property>
             <property name="styleSheet">
              <string notr="true">background-color: none;</string>
             </property>
             <property name="frameShape">
              <enum>QFrame::StyledPanel</enum>
             </property>
             <property name="frameShadow">
              <enum>QFrame::Raised</enum>
             </property>
            </widget>
           </item>
           <item>
            <widget class="QFrame" name="frame_20">
             <property name="minimumSize">
              <size>
               <width>680</width>
               <height>550</height>
              </size>
             </property>
             <property name="maximumSize">
              <size>
               <width>680</width>
               <height>550</height>
              </size>
             </property>
             <property name="styleSheet">
              <string notr="true">QFrame{
	
	background-color: rgb(218, 218, 218);
}
QPushButton{
	padding: 20px 10px;
	border: none;
	border-left: 2px solid transparent;
	border-bottom: 2px solid transparent;
	border-radius: 5px;
	background-color: rgb(68, 68, 102);
	color: rgb(140, 140, 140);
}
QPushButton:hover{
	background-color: rgb(0, 92, 157);
}
QPushButton:pressed {
	background-color:  rgb(0, 92, 157);
	border-bottom: 2px solid rgb(255, 165, 24);
}</string>
             </property>
             <property name="frameShape">
              <enum>QFrame::StyledPanel</enum>
             </property>
             <property name="frameShadow">
              <enum>QFrame::Raised</enum>
             </property>
             <widget class="QLabel" name="label_5">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>34</y>
                <width>653</width>
                <height>157</height>
               </rect>
              </property>
              <property name="font">
               <font>
                <pointsize>12</pointsize>
               </font>
              </property>
              <property name="text">
               <string>Connect to MySQL server</string>
              </property>
              <property name="alignment">
               <set>Qt::AlignCenter</set>
              </property>
             </widget>
             <widget class="QFrame" name="frame_21">
              <property name="geometry">
               <rect>
                <x>340</x>
                <y>360</y>
                <width>323</width>
                <height>157</height>
               </rect>
              </property>
              <property name="frameShape">
               <enum>QFrame::StyledPanel</enum>
              </property>
              <property name="frameShadow">
               <enum>QFrame::Raised</enum>
              </property>
              <widget class="QPushButton" name="connect_server">
               <property name="geometry">
                <rect>
                 <x>150</x>
                 <y>30</y>
                 <width>111</width>
                 <height>29</height>
                </rect>
               </property>
               <property name="text">
                <string>Next</string>
               </property>
              </widget>
              <widget class="QPushButton" name="cancel_server">
               <property name="geometry">
                <rect>
                 <x>20</x>
                 <y>30</y>
                 <width>111</width>
                 <height>31</height>
                </rect>
               </property>
               <property name="text">
                <string>Previous</string>
               </property>
              </widget>
             </widget>
             <widget class="QFrame" name="frame_22">
              <property name="geometry">
               <rect>
                <x>340</x>
                <y>197</y>
                <width>323</width>
                <height>157</height>
               </rect>
              </property>
              <property name="frameShape">
               <enum>QFrame::StyledPanel</enum>
              </property>
              <property name="frameShadow">
               <enum>QFrame::Raised</enum>
              </property>
              <widget class="QLineEdit" name="User">
               <property name="geometry">
                <rect>
                 <x>20</x>
                 <y>60</y>
                 <width>211</width>
                 <height>31</height>
                </rect>
               </property>
               <property name="styleSheet">
                <string notr="true">background-color: rgb(207, 219, 255);
color: rgb(182, 60, 182);
font: 12pt &quot;Century Gothic&quot;;</string>
               </property>
              </widget>
              <widget class="QLineEdit" name="Host">
               <property name="geometry">
                <rect>
                 <x>20</x>
                 <y>10</y>
                 <width>211</width>
                 <height>31</height>
                </rect>
               </property>
               <property name="styleSheet">
                <string notr="true">background-color: rgb(207, 219, 255);
color: rgb(182, 60, 182);
font: 12pt &quot;Century Gothic&quot;;</string>
               </property>
               <property name="text">
                <string/>
               </property>
              </widget>
              <widget class="QLineEdit" name="Password">
               <property name="geometry">
                <rect>
                 <x>20</x>
                 <y>110</y>
                 <width>211</width>
                 <height>31</height>
                </rect>
               </property>
               <property name="styleSheet">
                <string notr="true">background-color: rgb(207, 219, 255);
color: rgb(182, 60, 182);
font: 12pt &quot;Century Gothic&quot;;</string>
               </property>
              </widget>
             </widget>
             <widget class="QFrame" name="frame_23">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>197</y>
                <width>324</width>
                <height>157</height>
               </rect>
              </property>
              <property name="frameShape">
               <enum>QFrame::StyledPanel</enum>
              </property>
              <property name="frameShadow">
               <enum>QFrame::Raised</enum>
              </property>
              <widget class="QLabel" name="label_118">
               <property name="geometry">
                <rect>
                 <x>40</x>
                 <y>100</y>
                 <width>171</width>
                 <height>31</height>
                </rect>
               </property>
               <property name="styleSheet">
                <string notr="true">color: rgb(0, 0, 0);
font: 16pt &quot;Century Gothic&quot;;</string>
               </property>
               <property name="text">
                <string>Password</string>
               </property>
              </widget>
              <widget class="QLabel" name="label_121">
               <property name="geometry">
                <rect>
                 <x>40</x>
                 <y>10</y>
                 <width>171</width>
                 <height>31</height>
                </rect>
               </property>
               <property name="styleSheet">
                <string notr="true">color: rgb(0, 0, 0);
font: 16pt &quot;Century Gothic&quot;;</string>
               </property>
               <property name="text">
                <string>Host</string>
               </property>
              </widget>
              <widget class="QLabel" name="label_122">
               <property name="geometry">
                <rect>
                 <x>40</x>
                 <y>60</y>
                 <width>171</width>
                 <height>31</height>
                </rect>
               </property>
               <property name="styleSheet">
                <string notr="true">color: rgb(0, 0, 0);
font: 16pt &quot;Century Gothic&quot;;</string>
               </property>
               <property name="text">
                <string>User</string>
               </property>
              </widget>
             </widget>
             <widget class="QFrame" name="frame_24">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>360</y>
                <width>324</width>
                <height>157</height>
               </rect>
              </property>
              <property name="frameShape">
               <enum>QFrame::StyledPanel</enum>
              </property>
              <property name="frameShadow">
               <enum>QFrame::Raised</enum>
              </property>
             </widget>
            </widget>
           </item>
           <item>
            <widget class="QFrame" name="frame_25">
             <property name="minimumSize">
              <size>
               <width>0</width>
               <height>550</height>
              </size>
             </property>
             <property name="maximumSize">
              <size>
               <width>16777215</width>
               <height>550</height>
              </size>
             </property>
             <property name="font">
              <font>
               <family>Microsoft Yi Baiti</family>
              </font>
             </property>
             <property name="styleSheet">
              <string notr="true">background-color: none;</string>
             </property>
             <property name="frameShape">
              <enum>QFrame::StyledPanel</enum>
             </property>
             <property name="frameShadow">
              <enum>QFrame::Raised</enum>
             </property>
            </widget>
           </item>
          </layout>
         </widget>
        </item>
        <item>
         <widget class="QFrame" name="frame_27">
          <property name="styleSheet">
           <string notr="true"/>
          </property>
          <property name="frameShape">
           <enum>QFrame::StyledPanel</enum>
          </property>
          <property name="frameShadow">
           <enum>QFrame::Raised</enum>
          </property>
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
  <include location="E:/EDF/new_app/icons.qrc"/>
 </resources>
 <connections/>
</ui>
