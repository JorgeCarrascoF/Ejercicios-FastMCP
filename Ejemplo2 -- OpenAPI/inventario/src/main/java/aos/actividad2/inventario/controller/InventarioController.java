package aos.actividad2.inventario.controller;

import aos.actividad2.inventario.dto.MovimientoStockDTO;
import aos.actividad2.inventario.dto.ProductoDTO;
import aos.actividad2.inventario.exception.ProductoNotFound;
import aos.actividad2.inventario.service.InventarioService;
import java.util.List;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1/productos")
public class InventarioController {

  private final InventarioService inventarioService;

  public InventarioController(InventarioService inventarioService) {
    this.inventarioService = inventarioService;
  }

  @GetMapping
  public ResponseEntity<List<ProductoDTO>> getAllProductos() {
    return ResponseEntity.ok(inventarioService.getAllProductos());
  }

  @GetMapping("/{id}")
  public ResponseEntity<ProductoDTO> getProductoById(@PathVariable Long id) {
    try {
      return ResponseEntity.ok(inventarioService.getProductoById(id));
    } catch (ProductoNotFound e) {
      return ResponseEntity.notFound().build();
    }
  }

  @PostMapping
  public ResponseEntity<ProductoDTO> createProducto(
    @RequestBody ProductoDTO producto
  ) {
    ProductoDTO creado = inventarioService.saveProducto(producto);
    return ResponseEntity.status(201).body(creado);
  }

  @PatchMapping("/{id}")
  public ResponseEntity<ProductoDTO> updateProducto(
    @PathVariable Long id,
    @RequestBody ProductoDTO producto
  ) {
    try {
      ProductoDTO actualizado = inventarioService.actualizarProducto(
        id,
        producto
      );
      return ResponseEntity.ok(actualizado);
    } catch (ProductoNotFound e) {
      return ResponseEntity.notFound().build();
    }
  }

  @GetMapping("/{id}/check-stock/{cantidad}")
  public ResponseEntity<Boolean> comprobarStock(
    @PathVariable Long id,
    @PathVariable int cantidad
  ) {
    try {
      boolean disponible = inventarioService.comprobarStock(id, cantidad);
      return ResponseEntity.ok(disponible);
    } catch (ProductoNotFound e) {
      return ResponseEntity.notFound().build();
    }
  }

  @PostMapping("/{id}/movimientos")
  public ResponseEntity<MovimientoStockDTO> registrarMovimiento(
    @PathVariable Long id,
    @RequestBody MovimientoStockDTO request
  ) {
    try {
      MovimientoStockDTO movimiento = inventarioService.registrarMovimiento(
        id,
        request
      );
      return ResponseEntity.status(201).body(movimiento);
    } catch (ProductoNotFound e) {
      return ResponseEntity.notFound().build();
    }
  }

  @GetMapping("/{id}/movimientos")
  public ResponseEntity<List<MovimientoStockDTO>> getMovimientosByProductoId(
    @PathVariable Long id
  ) {
    try {
      List<MovimientoStockDTO> movimientos =
        inventarioService.getMovimientosByProductoId(id);
      return ResponseEntity.ok(movimientos);
    } catch (ProductoNotFound e) {
      return ResponseEntity.notFound().build();
    }
  }

  @DeleteMapping("/{id}")
  public ResponseEntity<Void> deleteProducto(@PathVariable Long id) {
    try {
      inventarioService.deleteProducto(id);
      return ResponseEntity.noContent().build();
    } catch (ProductoNotFound e) {
      return ResponseEntity.notFound().build();
    }
  }
}
