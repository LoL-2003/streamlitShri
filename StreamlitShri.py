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




import streamlit as st
import streamlit.components.v1 as components

st.title("Streamlit with Neural Network Style Animation")

# HTML code for neural network style animation using particles.js
neural_network_animation = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Neural Network Animation</title>
  <style>
  body, html {
    margin: 0;
    padding: 0;
    overflow: hidden;
  }
  #particles-js {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
  }
  </style>
</head>
<body>
  <div id="particles-js"></div>
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
          "value": "#00ff00"  # Set to green for a neural network effect
        },
        "shape": {
          "type": "circle",
          "stroke": {
            "width": 0,
            "color": "#000000"
          }
        },
        "opacity": {
          "value": 0.7,
          "random": false
        },
        "size": {
          "value": 3,
          "random": true
        },
        "line_linked": {
          "enable": true,
          "distance": 150,
          "color": "#00ff00",  # Same green color for the connecting lines
          "opacity": 0.6,
          "width": 2
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
            "distance": 200,
            "line_linked": {
              "opacity": 1
            }
          },
          "bubble": {
            "distance": 400,
            "size": 4,
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
</body>
</html>
"""

# Embedding the HTML into the Streamlit app
components.html(neural_network_animation, height=600)

st.write("Particles are connected with lines, creating a neural network effect.")

