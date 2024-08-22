# import streamlit as st
# import streamlit.components.v1 as components

# st.title("Streamlit with Cursor Tracking Particles")

# # HTML code with cursor animation using particles.js
# cursor_animation = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#   <meta charset="UTF-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1.0">
#   <title>Cursor Animation</title>
#   <style>
#   body, html {
#     margin: 0;
#     padding: 0;
#     overflow: hidden;
#   }
#   #particles-js {
#     position: absolute;
#     top: 0;
#     left: 0;
#     width: 100%;
#     height: 100%;
#     pointer-events: none;
#   }
#   </style>
# </head>
# <body>
#   <div id="particles-js"></div>
#   <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
#   <script>
#     particlesJS("particles-js", {
#       "particles": {
#         "number": {
#           "value": 100,
#           "density": {
#             "enable": true,
#             "value_area": 800
#           }
#         },
#         "color": {
#           "value": "#ffffff"
#         },
#         "shape": {
#           "type": "circle",
#           "stroke": {
#             "width": 0,
#             "color": "#000000"
#           }
#         },
#         "opacity": {
#           "value": 0.7,
#           "random": true
#         },
#         "size": {
#           "value": 3,
#           "random": true
#         },
#         "line_linked": {
#           "enable": false
#         },
#         "move": {
#           "enable": true,
#           "speed": 6,
#           "direction": "none",
#           "random": false,
#           "straight": false,
#           "out_mode": "out",
#           "bounce": false,
#           "attract": {
#             "enable": false
#           }
#         }
#       },
#       "interactivity": {
#         "detect_on": "window",
#         "events": {
#           "onhover": {
#             "enable": true,
#             "mode": "bubble"
#           },
#           "onclick": {
#             "enable": true,
#             "mode": "repulse"
#           }
#         },
#         "modes": {
#           "grab": {
#             "distance": 200,
#             "line_linked": {
#               "opacity": 1
#             }
#           },
#           "bubble": {
#             "distance": 250,
#             "size": 8,
#             "duration": 2,
#             "opacity": 0.8,
#             "speed": 3
#           },
#           "repulse": {
#             "distance": 400,
#             "duration": 0.4
#           },
#           "push": {
#             "particles_nb": 4
#           },
#           "remove": {
#             "particles_nb": 2
#           }
#         }
#       },
#       "retina_detect": true
#     });
#   </script>
# </body>
# </html>
# """

# # Embedding the HTML into the Streamlit app
# components.html(cursor_animation, height=600)

# st.write("Particles follow the cursor on hover and react on click.")











# import streamlit as st
# import streamlit.components.v1 as components

# def header_footer():
#     st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
    
#     st.markdown("""
#     <style>
#         .navbar-dark .navbar-nav .nav-link {
#             color: black !important;
#         }
#         .navbar-dark .navbar-brand img {
#             width: 150px;
#             height: 60px;
#         }
#     </style>
#     <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #DC84F3;">
#       <div class="container-fluid">
#         <a class="navbar-brand" href="#">
#           <img src="https://allthatsinteresting.com/wordpress/wp-content/uploads/2014/02/3D-Gifs-Nightmare.gif" alt="Brand Logo">
#         </a>
#         <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
#           <span class="navbar-toggler-icon"></span>
#         </button>
#         <div class="collapse navbar-collapse" id="collapsibleNavbar">
#           <ul class="navbar-nav">
#             <li class="nav-item">
#               <a class="nav-link" href="https://www.linkedin.com/in/adityapuri10/">Contact Us</a>
#             </li>
#             <li class="nav-item">
#               <a class="nav-link" href="https://github.com/Adi1042003">GitHub</a>
#             </li>
#             <li class="nav-item">
#               <a class="nav-link" href="https://drive.google.com/file/d/1lH_kcpl4t9HbF6uWTAc8PR431c1DzIAl/view?usp=sharing">About Project</a>
#             </li>
#           </ul>
#         </div>
#       </div>
#     </nav>
#     """, unsafe_allow_html=True)

#     hide_st_style = """
#     <style>
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     footer:after {content:'Made with ❤️ by ADITYA PURI';visibility: visible;display: block;}
#     .st-emotion-cache-cio0dv {
#         padding-left: 20%;
#         padding-right: 1rem;
#     }
#     header {visibility: hidden;}
#     </style>
#     """
#     st.markdown(hide_st_style, unsafe_allow_html=True)

# st.set_page_config(page_title="ADITYA")
# header_footer()


# st.title("Streamlit with Neural Network Style Animation Move/Click using Cursor in the Below space")

# # Simplified HTML and JavaScript for the neural network animation
# neural_network_animation = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#   <meta charset="UTF-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1.0">
#   <title>Neural Network Animation</title>
#   <style>
#   body, html {
#     margin: 0;
#     padding: 0;
#     overflow: hidden;
#     background-color: #000;
#   }
#   #particles-js {
#     position: absolute;
#     width: 100%;
#     height: 100%;
#   }
#   </style>
# </head>
# <body>
#   <div id="particles-js"></div>
#   <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
#   <script>
#     particlesJS("particles-js", {
#       "particles": {
#         "number": {
#           "value": 80,
#           "density": {
#             "enable": true,
#             "value_area": 800
#           }
#         },
#         "color": {
#           "value": "#FABC3F"
#         },
#         "shape": {
#           "type": "circle",
#           "stroke": {
#             "width": 0,
#             "color": "#000000"
#           }
#         },
#         "opacity": {
#           "value": 0.5,
#           "random": false
#         },
#         "size": {
#           "value": 3,
#           "random": true
#         },
#         "line_linked": {
#           "enable": true,
#           "distance": 150,
#           "color": "#FABC3F",
#           "opacity": 0.4,
#           "width": 1
#         },
#         "move": {
#           "enable": true,
#           "speed": 2,
#           "direction": "none",
#           "random": true,
#           "straight": false,
#           "out_mode": "out",
#           "bounce": false,
#           "attract": {
#             "enable": false
#           }
#         }
#       },
#       "interactivity": {
#         "detect_on": "canvas",
#         "events": {
#           "onhover": {
#             "enable": true,
#             "mode": "grab"
#           },
#           "onclick": {
#             "enable": true,
#             "mode": "push"
#           },
#           "resize": true
#         },
#         "modes": {
#           "grab": {
#             "distance": 140,
#             "line_linked": {
#               "opacity": 1
#             }
#           },
#           "bubble": {
#             "distance": 300,
#             "size": 7,
#             "duration": 2,
#             "opacity": 8,
#             "speed": 3
#           },
#           "repulse": {
#             "distance": 200,
#             "duration": 0.4
#           },
#           "push": {
#             "particles_nb": 4
#           },
#           "remove": {
#             "particles_nb": 2
#           }
#         }
#       },
#       "retina_detect": true
#     });
#   </script>
# </body>
# </html>
# """

# # Embed the HTML into the Streamlit app
# components.html(neural_network_animation, height=600)

# st.write("Particles are connected with lines, creating a neural network effect.")














import streamlit as st
import streamlit.components.v1 as components

def header_footer():
    st.markdown("""
    <style>
        .navbar-dark .navbar-nav .nav-link {
            color: black !important;
        }
        .navbar-dark .navbar-brand img {
            width: 150px;
            height: 60px;
        }
        .stApp {
            background: transparent !important;
        }
        /* Optional: styling content area */
        .st-emotion-cache-cio0dv {
            padding-left: 20%;
            padding-right: 1rem;
            background: rgba(255, 255, 255, 0.8); /* semi-transparent background */
            border-radius: 10px; /* rounded corners */
            padding: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

    hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    footer:after {content:'Made with ❤️ by ADITYA PURI';visibility: visible;display: block;}
    header {visibility: hidden;}
    </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

st.set_page_config(page_title="ADITYA")
header_footer()

st.title("Streamlit with Neural Network Style Animation")

# Neural Network Animation as Background
neural_network_animation = """
<div id="particles-js"></div>
<style>
  #particles-js {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    background-color: #000; /* Fallback color */
  }
  .stApp {
    position: relative;
    z-index: 1;
  }
</style>
<script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
<script>
  particlesJS("particles-js", {
    "particles": {
      "number": {
        "value": 80,
        "density": {
          "enable": true,
          "value_area": 800
        }
      },
      "color": {
        "value": "#FABC3F"
      },
      "shape": {
        "type": "circle",
        "stroke": {
          "width": 0,
          "color": "#000000"
        }
      },
      "opacity": {
        "value": 0.5,
        "random": false
      },
      "size": {
        "value": 3,
        "random": true
      },
      "line_linked": {
        "enable": true,
        "distance": 150,
        "color": "#FABC3F",
        "opacity": 0.4,
        "width": 1
      },
      "move": {
        "enable": true,
        "speed": 2,
        "direction": "none",
        "random": true,
        "straight": false,
        "out_mode": "out",
        "bounce": false,
        "attract": {
          "enable": false
        }
      }
    },
    "interactivity": {
      "detect_on": "canvas",
      "events": {
        "onhover": {
          "enable": true,
          "mode": "grab"
        },
        "onclick": {
          "enable": true,
          "mode": "push"
        },
        "resize": true
      },
      "modes": {
        "grab": {
          "distance": 140,
          "line_linked": {
            "opacity": 1
          }
        },
        "bubble": {
          "distance": 300,
          "size": 7,
          "duration": 2,
          "opacity": 8,
          "speed": 3
        },
        "repulse": {
          "distance": 200,
          "duration": 0.4
        },
        "push": {
          "particles_nb": 4
        },
        "remove": {
          "particles_nb": 2
        }
      }
    },
    "retina_detect": true
  });
</script>
"""

# Embed the HTML into the Streamlit app
components.html(neural_network_animation, height=0, width=0)

st.write("Particles are connected with lines, creating a neural network effect.")
