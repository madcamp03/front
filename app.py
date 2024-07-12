import streamlit as st
from streamlit_option_menu import option_menu

# 페이지 설정
st.set_page_config(
    page_title="My Sports App",
    page_icon="⚾",  # 흰 야구공 이모지 사용
    layout="wide",
    initial_sidebar_state="expanded",
)

# 사이드바 로고 설정
st.sidebar.markdown(
    """
    <div style="text-align: center;">
        <a href="?page=main">
            <span style="font-size: 48px;">⚾</span>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    choose = option_menu(
        "Menu",
        ["메인", "기록실", "오늘의 경기", "소속 팀", "마이페이지"],
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#ffffff"},
            "icon": {"color": "white", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#191848"},
        }
    )

# 각 메뉴에 대한 페이지 내용
if choose == "메인":

    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>three.js webgl - effects - ascii</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
    </head>

    <body>
        <script type="importmap">
            {
                "imports": {
                    "three": "https://cdn.jsdelivr.net/npm/three@0.137.5/build/three.module.js",
                    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.137.5/examples/jsm/"
                }
            }
        </script>

        <script type="module">

            import * as THREE from 'three';

            import { AsciiEffect } from 'three/addons/effects/AsciiEffect.js';
            import { TrackballControls } from 'three/addons/controls/TrackballControls.js';

            let camera, controls, scene, renderer, effect;

            let sphere, redLine1, redLine2, group;

            const start = Date.now();

            init();

            function init() {

                camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1, 1000 );
                camera.position.y = 150;
                camera.position.z = 500;

                scene = new THREE.Scene();
                scene.background = new THREE.Color( 0, 0, 0 );

                const pointLight1 = new THREE.PointLight( 0xffffff, 3, 0, 0 );
                pointLight1.position.set( 500, 500, 500 );
                scene.add( pointLight1 );

                const pointLight2 = new THREE.PointLight( 0xffffff, 1, 0, 0 );
                pointLight2.position.set( - 500, - 500, - 500 );
                scene.add( pointLight2 );

                group = new THREE.Group();

                // Create the sphere (baseball)
                sphere = new THREE.Mesh(
                    new THREE.SphereGeometry( 200, 32, 32 ), 
                    new THREE.MeshPhongMaterial( { color: 0xffffff, flatShading: true } )
                );
                group.add( sphere );

                // Create the red lines on the baseball
                const lineMaterial = new THREE.MeshBasicMaterial( { color: 0xff0000 } );
                const lineGeometry = new THREE.TorusGeometry( 200, 5, 16, 100 );

                redLine1 = new THREE.Mesh( lineGeometry, lineMaterial );
                redLine1.rotation.x = Math.PI / 2;
                group.add( redLine1 );

                redLine2 = new THREE.Mesh( lineGeometry, lineMaterial );
                redLine2.rotation.y = Math.PI / 2;
                group.add( redLine2 );

                scene.add(group);

                renderer = new THREE.WebGLRenderer();
                renderer.setSize( window.innerWidth, window.innerHeight );
                renderer.setAnimationLoop( animate );

                effect = new AsciiEffect( renderer, ' .:-+*=%@#', { invert: true } );
                effect.setSize( window.innerWidth, window.innerHeight );
                effect.domElement.style.color = 'black';
                effect.domElement.style.backgroundColor = 'white';

                document.body.appendChild( effect.domElement );

                controls = new TrackballControls( camera, effect.domElement );

                window.addEventListener( 'resize', onWindowResize );

                // Wait for the ASCII lines to be rendered, then change the color of specific lines
                setTimeout(() => {
                    const asciiLines = effect.domElement.querySelectorAll('tr');
                    if (asciiLines.length > 5) {
                        asciiLines[5].style.color = 'red';
                        asciiLines[6].style.color = 'red';
                    }
                    if (asciiLines.length > 15) {
                        asciiLines[15].style.color = 'red';
                        asciiLines[16].style.color = 'red';
                    }
                }, 1000); // Adjust the timeout as needed for rendering completion

            }

            function onWindowResize() {

                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();

                renderer.setSize( window.innerWidth, window.innerHeight );
                effect.setSize( window.innerWidth, window.innerHeight );

            }

            function animate() {

                const timer = Date.now() - start;

                group.position.y = Math.abs( Math.sin( timer * 0.002 ) ) * 150;
                group.rotation.x = timer * 0.0003;
                group.rotation.z = timer * 0.0002;

                controls.update();

                effect.render( scene, camera );

            }

        </script>

    </body>
    </html>
    """

    # Streamlit에서 HTML과 JavaScript 코드 실행
    st.components.v1.html(html_code, height=600)

elif choose == "기록실":
    st.write("기록실 페이지 내용")
elif choose == "오늘의 경기":
    st.write("오늘의 경기 페이지 내용")
elif choose == "소속 팀":
    st.write("소속 팀 페이지 내용")
elif choose == "마이페이지":
    st.write("마이페이지 내용")
