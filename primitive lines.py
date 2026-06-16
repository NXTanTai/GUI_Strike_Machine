# Source - https://stackoverflow.com/q/77795052
# Posted by Meliord, modified by community. See post 'Timeline' for change history
# Retrieved 2026-06-16, License - CC BY-SA 4.0

from PySide6.QtCore import QTimer, QByteArray
from PySide6.QtGui import QVector3D, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.Qt3DCore import Qt3DCore
from PySide6.Qt3DExtras import Qt3DExtras
from PySide6.Qt3DRender import Qt3DRender
import struct

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Qt3D Primitive Lines')
        self.setGeometry(100, 100, 1280, 720)

        # Set up the 3D view
        self.view = Qt3DExtras.Qt3DWindow()
        self.view.defaultFrameGraph().setClearColor(QColor(255,255,255))
        self.container = QWidget.createWindowContainer(self.view)
        self.setCentralWidget(self.container)

        # Set up the 3D scene
        self.root = Qt3DCore.QEntity()
        self.view.setRootEntity(self.root)
        # Create a 3D entity for the line
        self.line_entity = Qt3DCore.QEntity(self.root)
        line_geometry = Qt3DCore.QGeometry(self.line_entity)

        # Create a custom line geometry
        vertex_data = [QVector3D(0.0, 0.0, 0.0), QVector3D(1.0, 0.0, 0.0), QVector3D(1.0, 1.0, 0.0)]
        vertex_byteArray = QByteArray()

        for vector in vertex_data:
            vertex_byteArray.append(struct.pack('fff', vector.x(), vector.y(), vector.z()))

        vertex_buffer = Qt3DCore.QBuffer(line_geometry)
        vertex_buffer.setData(vertex_byteArray)

        # Create a QAttribute to store the vertex data
        vertex_attribute = Qt3DCore.QAttribute()
        vertex_attribute.setName(Qt3DCore.QAttribute.defaultPositionAttributeName())
        vertex_attribute.setAttributeType(Qt3DCore.QAttribute.AttributeType.VertexAttribute)
        vertex_attribute.setVertexBaseType(Qt3DCore.QAttribute.VertexBaseType.Float)
        vertex_attribute.setBuffer(vertex_buffer)
        vertex_attribute.setVertexSize(3)  # 3 components (X, Y, Z) per vertex
        vertex_attribute.setByteOffset(0)
        vertex_attribute.setByteStride(3 * 4)  # 3 components * 4 bytes for float
        vertex_attribute.setCount(len(vertex_data))

        line_geometry.addAttribute(vertex_attribute)

        # Create connections between vertices
        index_data = [0, 1, 2]
        index_bytes = QByteArray()
        for idx in index_data:
            index_bytes.append(struct.pack('I', idx))

        index_buffer = Qt3DCore.QBuffer(line_geometry)
        index_buffer.setData(index_bytes)

        # Create a QAttribute to store the index data
        index_attribute = Qt3DCore.QAttribute()
        index_attribute.setAttributeType(Qt3DCore.QAttribute.AttributeType.IndexAttribute)
        index_attribute.setVertexBaseType(Qt3DCore.QAttribute.VertexBaseType.UnsignedInt)
        index_attribute.setBuffer(index_buffer)
        index_attribute.setByteOffset(0)
        index_attribute.setByteStride(4)
        index_attribute.setCount(len(index_data))

        line_geometry.addAttribute(index_attribute)

        # Create a line material
        self.line_material = Qt3DExtras.QPhongMaterial(self.root)
        self.line_material.setAmbient(QColor(255,0,0))

        # Create a line renderer
        self.line_renderer = Qt3DRender.QGeometryRenderer(self.root)
        self.line_renderer.setPrimitiveType(Qt3DRender.QGeometryRenderer.LineStrip)
        self.line_renderer.setGeometry(line_geometry)
        self.line_renderer.setVertexCount(len(vertex_data))

        self.line_entity.addComponent(self.line_renderer)
        self.line_entity.addComponent(self.line_material)

        # Set up camera
        self.camera_entity = self.view.camera()
        # camera_entity.lens().setPerspectiveProjection(45.0, 16.0/9.0, 0.1, 1000.0)
        self.camera_entity.setPosition(QVector3D(2, 2, 5))
        self.camera_entity.setViewCenter(QVector3D(0, 0, 0))

        # Add a light to the scene
        self.light_entity = Qt3DCore.QEntity(self.root)
        self.light = Qt3DRender.QPointLight(self.light_entity)
        self.light.setIntensity(1.0)
        self.light_entity.addComponent(self.light)
        light_transform = Qt3DCore.QTransform()
        light_transform.setTranslation(QVector3D(5, 5, 5))
        self.light_entity.addComponent(light_transform)

        # Set up orbit controller
        self.orbit_controller = Qt3DExtras.QOrbitCameraController(self.root)
        self.orbit_controller.setLinearSpeed(2.0)
        self.orbit_controller.setLookSpeed(100.0)
        self.orbit_controller.setCamera(self.camera_entity)

        # Add vertices after a delay
        QTimer.singleShot(2000, self.add_more_vertices)

        self.show()

    def add_more_vertices(self):
        print("add_more_vertices called (not fully implemented)")
        # TODO: implement dynamic vertex addition if needed

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    app.exec()
