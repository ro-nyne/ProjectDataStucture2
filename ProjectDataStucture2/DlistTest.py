import unittest
from DoublyLinkedList import Dlist, Node


class NodeTest(unittest.TestCase):
    def test_node_is_a_class(self):
        self.assertIsInstance(Node, object)

    def test_node_has_right_properties(self):
        node = Node('a', 'b', 'c')
        self.assertEqual(node.data, 'a')
        self.assertEqual(node.prev, 'b')
        self.assertEqual(node.next, 'c')

    def test_print_node(self):
        node = Node(2, None, None)
        self.assertEqual(
            str(node), "{'data': 2, 'prev': None, 'next': None}")


class DlistTest(unittest.TestCase):
    def test_list_is_a_class(self):
        self.assertIsInstance(Dlist, object)

    def test_insert_first(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(1)
        self.assertEqual(linkedlist.head.data, 1)
        linkedlist.insert_at_head(2)
        self.assertEqual(linkedlist.head.data, 2)

    def test_length(self):
        linkedlist = Dlist()
        self.assertEqual(linkedlist.get_length(), 0)
        linkedlist.insert_at_head(1)
        linkedlist.insert_at_head(1)
        linkedlist.insert_at_head(1)
        linkedlist.insert_at_head(1)
        self.assertEqual(linkedlist.get_length(), 4)

    def test_get_first(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(1)
        self.assertEqual(linkedlist.head.data, 1)
        linkedlist.insert_at_head(2)
        self.assertEqual(linkedlist.head.data, 2)

    def test_get_last(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(4)
        self.assertEqual(linkedlist.get_tail().data, 4)

        linkedlist.insert_at_head(2)

        self.assertEqual(linkedlist.get_tail().data, 4)

        linkedlist.insert_at_tail(7)

        self.assertEqual(linkedlist.get_tail().data, 7)

    def test_clear(self):
        linkedlist = Dlist()
        self.assertEqual(linkedlist.get_length(), 0)
        linkedlist.insert_at_head(1)
        linkedlist.insert_at_head(2)
        self.assertEqual(linkedlist.head.data, 2)
        linkedlist.insert_at_head(6)
        self.assertEqual(linkedlist.get_length(), 3)
        linkedlist.clear()
        self.assertEqual(linkedlist.get_length(), 0)

    def test_remove_first(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(1)
        linkedlist.insert_at_head(5)
        linkedlist.insert_at_head(7)
        self.assertEqual(linkedlist.get_length(), 3)
        linkedlist.insert_at_head(3)
        self.assertEqual(linkedlist.get_length(), 4)
        linkedlist.remove_at_head()
        self.assertEqual(linkedlist.get_length(), 3)
        self.assertEqual(linkedlist.get_head().data, 7)
        linkedlist.remove_at_head()
        self.assertEqual(linkedlist.get_length(), 2)
        self.assertEqual(linkedlist.get_head().data, 5)

    def test_remove_first_none(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(2)
        self.assertEqual(linkedlist.get_length(), 1)
        linkedlist.remove_at_head()
        self.assertIsNone(linkedlist.head)

    def test_remove_last(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(2)
        linkedlist.insert_at_head(6)
        linkedlist.insert_at_head(8)
        self.assertTrue(linkedlist.get_length(), 3)
        self.assertTrue(linkedlist.get_tail().data, 2)
        linkedlist.remove_at_tail()
        self.assertEqual(linkedlist.get_length(), 2)
        self.assertTrue(linkedlist.get_tail().data, 6)
        self.assertTrue(linkedlist.head.data, 8)

    def test_remove_last_no_error(self):
        linkedlist = Dlist()
        linkedlist.remove_at_tail()
        self.assertIsNone(linkedlist.head)

    def test_remove_last_node(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(2)
        self.assertEqual(linkedlist.get_length(), 1)
        linkedlist.remove_at_tail()
        self.assertIsNone(linkedlist.head)

    def test_insert_last(self):
        linkedlist = Dlist()
        linkedlist.insert_at_tail(5)
        self.assertEqual(linkedlist.get_length(), 1)
        linkedlist.insert_at_head(7)
        linkedlist.insert_at_tail(11)
        self.assertEqual(linkedlist.get_tail().data, 11)

    def test_get_at(self):
        linkedlist = Dlist()
        self.assertIsNone(linkedlist.get_at(10))

        linkedlist.insert_at_head(2)
        linkedlist.insert_at_head(6)
        linkedlist.insert_at_head(8)
        linkedlist.insert_at_head(4)

        self.assertEqual(linkedlist.get_at(0).data, 4)
        self.assertEqual(linkedlist.get_at(1).data, 8)
        self.assertEqual(linkedlist.get_at(2).data, 6)
        self.assertEqual(linkedlist.get_at(3).data, 2)

    def test_get_at_magic_method(self):
        linkedlist = Dlist()
        linkedlist = Dlist()
        self.assertIsNone(linkedlist[10])

        linkedlist.insert_at_head(2)
        linkedlist.insert_at_head(6)
        linkedlist.insert_at_head(8)
        linkedlist.insert_at_head(4)

        self.assertEqual(linkedlist[0].data, 4)
        self.assertEqual(linkedlist[1].data, 8)
        self.assertEqual(linkedlist[2].data, 6)
        self.assertEqual(linkedlist[3].data, 2)

    def test_remove_at_doesnt_crash_empty(self):
        linkedlist = Dlist()
        linkedlist.remove_at(10)
        self.assertIsNone(linkedlist.head)

    def test_remove_at_doesnt_crash_out_of_bounds(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(3)
        linkedlist.remove_at(4)
        self.assertEqual(linkedlist.head.data, 3)

    def test_remove_at_first(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(4)
        linkedlist.insert_at_head(7)
        linkedlist.insert_at_head(3)
        linkedlist.insert_at_head(1)
        self.assertEqual(linkedlist.get_at(0).data, 1)
        linkedlist.remove_at(0)
        self.assertEqual(linkedlist.get_at(0).data, 3)

    def test_remove_at_index(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(4)
        linkedlist.insert_at_head(7)
        linkedlist.insert_at_head(3)
        linkedlist.insert_at_head(1)
        self.assertEqual(linkedlist.get_at(1).data, 3)
        linkedlist.remove_at(1)
        self.assertEqual(linkedlist.get_at(1).data, 7)

    def test_remove_at_last(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(4)
        linkedlist.insert_at_head(7)
        linkedlist.insert_at_head(3)
        linkedlist.insert_at_head(1)

        self.assertEqual(linkedlist.get_tail().data, 4)

        linkedlist.remove_at(3)

        self.assertEqual(linkedlist.get_tail().data, 7)

    def test_insert_at_start_when_empty(self):
        linkedlist = Dlist()
        linkedlist.insert_at(0, 10)
        self.assertEqual(linkedlist.get_head().data, 10)

    def test_insert_at_start_when_list_has_elements(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(4)
        linkedlist.insert_at_head(8)
        linkedlist.insert_at_head(9)
        linkedlist.insert_at(0, 10)
        self.assertEqual(linkedlist.get_head().data, 10)
        self.assertEqual(linkedlist.get_at(1).data, 9)
        self.assertEqual(linkedlist.get_at(2).data, 8)
        self.assertEqual(linkedlist.get_at(3).data, 4)

    def test_insert_at_middle(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(5)
        linkedlist.insert_at_head(7)
        linkedlist.insert_at_head(3)
        linkedlist.insert_at_head(2)
        linkedlist.insert_at(2, 11)
        self.assertEqual(linkedlist.get_at(0).data, 2)
        self.assertEqual(linkedlist.get_at(1).data, 3)
        self.assertEqual(linkedlist.get_at(2).data, 11)
        self.assertEqual(linkedlist.get_at(3).data, 7)
        self.assertEqual(linkedlist.get_at(4).data, 5)

    def test_insert_at_last(self):
        linkedlist = Dlist()
        linkedlist.insert_at_tail(5)
        linkedlist.insert_at_tail(8)
        linkedlist.insert_at_tail(3)
        linkedlist.insert_at(3, 14)
        self.assertEqual(linkedlist.get_at(0).data, 5)
        self.assertEqual(linkedlist.get_at(1).data, 8)
        self.assertEqual(linkedlist.get_at(2).data, 3)
        self.assertEqual(linkedlist.get_at(3).data, 14)

    def test_insert_at_when_out_of_bounds(self):
        linkedlist = Dlist()
        linkedlist.insert_at_tail(4)
        linkedlist.insert_at_tail(11)
        linkedlist.insert_at(20, 17)
        self.assertEqual(linkedlist.get_at(0).data, 4)
        self.assertEqual(linkedlist.get_at(1).data, 11)
        self.assertEqual(linkedlist.get_at(2).data, 17)

    def test_for_each(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(5)
        linkedlist.insert_at_head(7)
        linkedlist.insert_at_head(9)
        linkedlist.insert_at_head(11)

        linkedlist.for_each(lambda num, index: num + 10)

        self.assertTrue(linkedlist.get_at(0).data, 11)
        self.assertTrue(linkedlist.get_at(1).data, 9)
        self.assertTrue(linkedlist.get_at(2).data, 7)
        self.assertTrue(linkedlist.get_at(3).data, 5)

    def test_reverse(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(4)
        linkedlist.insert_at_head(8)
        linkedlist.insert_at_head(11)
        linkedlist.insert_at_head(5)

        self.assertEqual(linkedlist.get_at(0).data, 5)
        self.assertEqual(linkedlist.get_at(1).data, 11)
        self.assertEqual(linkedlist.get_at(2).data, 8)
        self.assertEqual(linkedlist.get_at(3).data, 4)
        self.assertEqual(linkedlist.head.data, 5)

        linkedlist.reverse_node()

        self.assertEqual(linkedlist.get_at(0).data, 4)
        self.assertEqual(linkedlist.get_at(1).data, 8)
        self.assertEqual(linkedlist.get_at(2).data, 11)
        self.assertEqual(linkedlist.get_at(3).data, 5)
        self.assertEqual(linkedlist.head.data, 4)

    def test_find_index(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(5)
        linkedlist.insert_at_head(1)
        linkedlist.insert_at_head(2)
        linkedlist.insert_at_head(3)
        linkedlist.insert_at_head(9)

        self.assertEqual(linkedlist.find_index(9), 0)
        self.assertEqual(linkedlist.find_index(3), 1)
        self.assertEqual(linkedlist.find_index(2), 2)
        self.assertEqual(linkedlist.find_index(1), 3)
        self.assertEqual(linkedlist.find_index(5), 4)
        self.assertEqual(linkedlist.find_index(11), -1)

    def test_contains(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(1)
        linkedlist.insert_at_head(2)
        linkedlist.insert_at_head(3)
        linkedlist.insert_at_head(4)
        linkedlist.insert_at_head(5)

        self.assertTrue(linkedlist.contains(1))
        self.assertTrue(linkedlist.contains(2))
        self.assertTrue(linkedlist.contains(3))
        self.assertTrue(linkedlist.contains(4))
        self.assertTrue(linkedlist.contains(5))
        self.assertFalse(linkedlist.contains(11))
        self.assertFalse(linkedlist.contains(9))
        self.assertFalse(linkedlist.contains(6))

    def test_find(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(1)
        linkedlist.insert_at_head(2)
        linkedlist.insert_at_head(5)
        linkedlist.insert_at_head(4)
        linkedlist.insert_at_head(9)

        self.assertEqual(linkedlist.find(1).data, 1)
        self.assertEqual(linkedlist.find(5).data, 5)
        self.assertEqual(linkedlist.find(2).data, 2)
        self.assertEqual(linkedlist.find(9).data, 9)
        self.assertIsNone(linkedlist.find(15))

    def test_sort(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(5)
        linkedlist.insert_at_head(2)
        linkedlist.insert_at_head(1)
        linkedlist.insert_at_head(4)
        linkedlist.insert_at_head(9)
        linkedlist.insert_at_head(22)
        linkedlist.insert_at_head(3)
        linkedlist.insert_at_head(11)

        linkedlist.bubble_sort_node(type='asc')

        self.assertEqual(linkedlist.get_at(0).data, 1)
        self.assertEqual(linkedlist.get_at(1).data, 2)
        self.assertEqual(linkedlist.get_at(2).data, 3)
        self.assertEqual(linkedlist.get_at(3).data, 4)
        self.assertEqual(linkedlist.get_at(4).data, 5)
        self.assertEqual(linkedlist.get_at(5).data, 9)
        self.assertEqual(linkedlist.get_at(6).data, 11)
        self.assertEqual(linkedlist.get_at(7).data, 22)

        linkedlist.bubble_sort_node(type='desc')

        self.assertEqual(linkedlist.get_at(0).data, 22)
        self.assertEqual(linkedlist.get_at(1).data, 11)
        self.assertEqual(linkedlist.get_at(2).data, 9)
        self.assertEqual(linkedlist.get_at(3).data, 5)
        self.assertEqual(linkedlist.get_at(4).data, 4)
        self.assertEqual(linkedlist.get_at(5).data, 3)
        self.assertEqual(linkedlist.get_at(6).data, 2)
        self.assertEqual(linkedlist.get_at(7).data, 1)

    def test_is_empty(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(5)
        linkedlist.insert_at_head(5)

        self.assertFalse(linkedlist.is_empty())

        linkedlist.remove_at_tail()

        self.assertFalse(linkedlist.is_empty())

        linkedlist.clear()

        self.assertTrue(linkedlist.is_empty())

    def test_prev_and_next(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(4)
        linkedlist.insert_at_head(6)
        linkedlist.insert_at_head(8)

        node = linkedlist.get_at(1)
        previous = node.prev
        next = node.next

        self.assertEqual(node.data, 6)
        self.assertEqual(previous.data, 8)
        self.assertEqual(next.data, 4)

    def test_prev_and_next_reverse(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(4)
        linkedlist.insert_at_head(6)
        linkedlist.insert_at_head(8)
        linkedlist.insert_at_head(9)
        linkedlist.insert_at_head(5)

        self.assertEqual(linkedlist.get_at(0).data, 5)
        self.assertEqual(linkedlist.get_at(1).data, 9)
        self.assertEqual(linkedlist.get_at(2).data, 8)
        self.assertEqual(linkedlist.get_at(3).data, 6)
        self.assertEqual(linkedlist.get_at(4).data, 4)

        self.assertIsNone(linkedlist.get_at(0).prev)
        self.assertEqual(linkedlist.get_at(0).data, 5)
        self.assertEqual(linkedlist.get_at(0).next.data, 9)

        self.assertEqual(linkedlist.get_at(1).prev.data, 5)
        self.assertEqual(linkedlist.get_at(1).data, 9)
        self.assertEqual(linkedlist.get_at(1).next.data, 8)

        self.assertEqual(linkedlist.get_at(2).prev.data, 9)
        self.assertEqual(linkedlist.get_at(2).data, 8)
        self.assertEqual(linkedlist.get_at(2).next.data, 6)

        self.assertEqual(linkedlist.get_at(3).prev.data, 8)
        self.assertEqual(linkedlist.get_at(3).data, 6)
        self.assertEqual(linkedlist.get_at(3).next.data, 4)

        self.assertEqual(linkedlist.get_at(4).prev.data, 6)
        self.assertEqual(linkedlist.get_at(4).data, 4)
        self.assertIsNone(linkedlist.get_at(4).next)

        linkedlist.reverse_node()

        self.assertEqual(linkedlist.get_at(0).data, 4)
        self.assertEqual(linkedlist.get_at(1).data, 6)
        self.assertEqual(linkedlist.get_at(2).data, 8)
        self.assertEqual(linkedlist.get_at(3).data, 9)
        self.assertEqual(linkedlist.get_at(4).data, 5)

        self.assertIsNone(linkedlist.get_at(0).prev)
        self.assertEqual(linkedlist.get_at(0).data, 4)
        self.assertEqual(linkedlist.get_at(0).next.data, 6)

        self.assertEqual(linkedlist.get_at(1).prev.data, 4)
        self.assertEqual(linkedlist.get_at(1).data, 6)
        self.assertEqual(linkedlist.get_at(1).next.data, 8)

        self.assertEqual(linkedlist.get_at(2).prev.data, 6)
        self.assertEqual(linkedlist.get_at(2).data, 8)
        self.assertEqual(linkedlist.get_at(2).next.data, 9)

        self.assertEqual(linkedlist.get_at(3).prev.data, 8)
        self.assertEqual(linkedlist.get_at(3).data, 9)
        self.assertEqual(linkedlist.get_at(3).next.data, 5)

        self.assertEqual(linkedlist.get_at(4).prev.data, 9)
        self.assertEqual(linkedlist.get_at(4).data, 5)
        self.assertIsNone(linkedlist.get_at(4).next)

    def test_find_midpoint(self):
        linkedlist = Dlist()

        linkedlist.insert_at_head(4)
        linkedlist.insert_at_head(6)
        linkedlist.insert_at_head(8)
        linkedlist.insert_at_head(9)
        linkedlist.insert_at_head(5)

        node = linkedlist.find_midpoint()

        self.assertEqual(node.data, 8)
        self.assertEqual(node.prev.data, 9)
        self.assertEqual(node.next.data, 6)

        linkedlist.insert_at_tail(7)
        linkedlist.insert_at_tail(11)
        linkedlist.insert_at_head(44)

        node = linkedlist.find_midpoint()

        self.assertEqual(node.data, 8)
        self.assertEqual(node.prev.data, 9)
        self.assertEqual(node.next.data, 6)

        linkedlist.insert_at_head(33)
        linkedlist.insert_at_head(14)
        linkedlist.insert_at_head(12)
        linkedlist.insert_at_tail(17)
        linkedlist.insert_at_tail(19)

        node = linkedlist.find_midpoint()

        self.assertEqual(node.data, 8)
        self.assertEqual(node.prev.data, 9)
        self.assertEqual(node.next.data, 6)

    def test_step_back_from_tail(self):
        linkedlist = Dlist()

        linkedlist.insert_at_head(4)
        linkedlist.insert_at_head(6)
        linkedlist.insert_at_head(8)
        linkedlist.insert_at_head(9)
        linkedlist.insert_at_head(5)

        node = linkedlist.step_back_from_tail(0)

        self.assertEqual(node.data, 4)
        self.assertEqual(node.prev.data, 6)
        self.assertIsNone(node.next)

        node = linkedlist.step_back_from_tail(3)

        self.assertEqual(node.data, 9)
        self.assertEqual(node.prev.data, 5)
        self.assertEqual(node.next.data, 8)

        node = linkedlist.step_back_from_tail(1)

        self.assertEqual(node.data, 6)
        self.assertEqual(node.prev.data, 8)
        self.assertEqual(node.next.data, 4)

    def test_step_forward_from_head(self):
        linkedlist = Dlist()

        linkedlist = Dlist()
        linkedlist.insert_at_head(4)
        linkedlist.insert_at_head(6)
        linkedlist.insert_at_head(8)
        linkedlist.insert_at_head(9)
        linkedlist.insert_at_head(5)

        node = linkedlist.step_forward_from_head(0)

        self.assertEqual(node.data, 5)
        self.assertIsNone(node.prev)
        self.assertEqual(node.next.data, 9)

        node = linkedlist.step_forward_from_head(3)

        self.assertEqual(node.data, 6)
        self.assertEqual(node.prev.data, 8)
        self.assertEqual(node.next.data, 4)

        node = linkedlist.step_forward_from_head(1)

        self.assertEqual(node.data, 9)
        self.assertEqual(node.prev.data, 5)
        self.assertEqual(node.next.data, 8)

    def test_is_circular(self):
        linkedlist = Dlist()

        linkedlist.insert_at_head(4)
        linkedlist.insert_at_head(6)
        linkedlist.insert_at_head(8)
        linkedlist.insert_at_head(9)
        linkedlist.insert_at_head(5)

        self.assertFalse(linkedlist.is_circular())

        linkedlist.tail.next = linkedlist.get_at(3)

        self.assertEqual(linkedlist.tail.next.data, 6)
        self.assertEqual(linkedlist.tail.next.next.data, 4)

        self.assertTrue(linkedlist.is_circular())

        linkedlist.tail.next = None

        self.assertFalse(linkedlist.is_circular())
        
    def test_remove_data(self):
        linkedlist = Dlist()
        linkedlist.insert_at_head(4)
        linkedlist.insert_at_head(6)
        linkedlist.insert_at_head(8)
        linkedlist.insert_at_head(9)
        linkedlist.insert_at_head(5)
        self.assertEqual(linkedlist.get_length(), 5)
        linkedlist.remove_data(6)
        self.assertEqual(linkedlist.get_length(), 4)
        self.assertTrue(linkedlist.get_head().data, 4)
        self.assertIsNone(linkedlist.remove_data(1))

if __name__ == '__main__':
    unittest.main()